import ctypes
import difflib
import inspect
import os
import subprocess
import sys
import webbrowser
from threading import Thread
import qdarkstyle

from PySide6 import QtCore
from PySide6.QtCore import QObject, Qt, QFileInfo
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QApplication, QWidget, QFileDialog

from ui_Evaluator import Ui_MainWindow


class MySignals(QObject):
    text_print = QtCore.Signal(str)


global_ms = MySignals()


def _async_raise(tid, exctype):
    tid = ctypes.c_long(tid)
    if not inspect.isclass(exctype):
        exctype = type(exctype)
    res = ctypes.pythonapi.PyThreadState_SetAsyncExc(tid, ctypes.py_object(exctype))
    if res == 0:
        raise ValueError("invalid thread id")
    elif res != 1:
        ctypes.pythonapi.PyThreadState_SetAsyncExc(tid, None)
        raise SystemError("PyThreadState_SetAsyncExc failed")


def stop_thread(thread):
    if thread is None:
        return
    _async_raise(thread.ident, SystemExit)


class Evaluator(QWidget):
    def __init__(self):
        super().__init__()
        self.thread = None
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.start_button.clicked.connect(self.start_run)
        self.ui.end_button.clicked.connect(self.stop_run)
        self.ui.clear_button.clicked.connect(self.clear)
        self.ui.choose_file.clicked.connect(self.choose_file)
        self.ui.choose_path.clicked.connect(self.choose_path)
        global_ms.text_print.connect(self.printToGui)

    def printToGui(self, text):
        self.ui.outputs.append(str(text))
        self.ui.outputs.ensureCursorVisible()

    def clear(self):
        self.ui.outputs.clear()
        self.ui.outputs.setAlignment(Qt.AlignCenter)

    def start_run(self):
        self.ui.start_button.setEnabled(False)
        self.thread = Thread(target=self.start_evaluate)
        self.thread.start()

    def stop_run(self):
        if self.thread is not None:
            stop_thread(self.thread)
            self.ui.start_button.setEnabled(True)

    def choose_file(self):
        file_info, file_type = QFileDialog.getOpenFileName(self, "选择数据生成文件", "/..",
                                                           "Python Files (*.py);;Python Files (*.py)")
        fileinfo = QFileInfo(file_info)
        self.file_path = fileinfo.path()
        self.file_name = fileinfo.baseName()
        self.ui.file_name.setText(self.file_name)

    def choose_path(self):
        self.path = QFileDialog.getExistingDirectory(self, "选择jar包所在文件夹", "/..")
        self.ui.path.setText(self.path)

    def start_evaluate(self):
        sys.path.append(self.file_path)
        file = __import__(self.file_name)
        method_name = self.ui.method_name.text()
        temp_tle = self.ui.tle_time.text()
        if temp_tle == "":
            tle_time = 2147483647
        else:
            tle_time = float(temp_tle)
        args = self.ui.args.toPlainText().split("\n")
        jars = self.ui.jars.toPlainText().split("\n")
        data_generate = getattr(file, method_name)
        func_str = 'data_generate('
        for i in range(len(args) - 1):
            func_str += args[i] + ','
        func_str += args[-1] + ')'
        case = 1
        while True:
            data = eval(func_str)
            os.chdir(self.path)
            file = open('input.txt', 'w')
            for line in data:
                file.write(line + '\n')
            file.close()
            if self.test(self.path, jars, case, tle_time) is False:
                return
            case += 1

    def test(self, path: str, jars: list, num: int, time_limit: float) -> bool:
        def threadFunc(text: str):
            global_ms.text_print.emit(text)

        def show_result():
            webbrowser.open_new_tab('result.html')

        thread = Thread(target=threadFunc,
                        args=(str('----- TEST CASE ' + str(num) + ' BEGIN -----\n' + 'TIME'),))
        thread.start()
        os.chdir(path)
        for jar in jars:
            os.environ["COMSPEC"] = 'powershell'
            p = subprocess.Popen(
                'Measure-Command{Get-Content input.txt | java -jar ' + jar + '.jar > ' + jar + '.txt}',
                shell=True, stdout=subprocess.PIPE)
            p.wait()
            time_list = p.stdout.read()
            sorted_list = time_list.decode('utf-8').strip().split('\n')
            time_used = float(sorted_list[9].split(": ")[1])
            thread = Thread(target=threadFunc,
                            args=(str(jar + ' used : ' + str(time_used) + 's'),))
            thread.start()
            if time_used >= time_limit:
                thread = Thread(target=threadFunc,
                                args=(str(jar + ' is TLE'),))
                thread.start()
                self.ui.start_button.setEnabled(True)
                return False
        thread = Thread(target=threadFunc,
                        args=(str('RESULT'),))
        thread.start()
        pre = jars[0]
        for i in range(1, len(jars)):
            now = jars[i]
            pre_file = open(pre + '.txt', 'r', encoding='utf-16le').readlines()
            now_file = open(now + '.txt', 'r', encoding='utf-16le').readlines()
            tmp = difflib.context_diff(pre_file, now_file)
            try:
                next(tmp)
            except StopIteration:
                pre = jars[i]
                continue
            dif = difflib.HtmlDiff().make_file(pre_file, now_file, context=True)
            f = open('result.html', 'w', encoding='utf-8')
            f.write(dif)
            thread = Thread(target=threadFunc,
                            args=(
                                str(jars[i] + ' is different with ' + pre),))
            thread.start()
            result_thread = Thread(target=show_result)
            result_thread.start()
            self.ui.start_button.setEnabled(True)
            return False
        thread = Thread(target=threadFunc,
                        args=(
                            str('All answers are identical\n' + '------ TEST CASE ' + str(num) + ' END ------\n\n'),))
        thread.start()
        return True


if __name__ == "__main__":
    app = QApplication([])
    app.setWindowIcon(QIcon('windowlogo.png'))
    evaluator = Evaluator()
    app.setStyleSheet(qdarkstyle.load_stylesheet(qt_api='pyside6'))
    evaluator.show()
    sys.exit(app.exec())
