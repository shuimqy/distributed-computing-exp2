import grpc
import hospital_pb2
import hospital_pb2_grpc
from PySide6.QtWidgets import (
    QWidget,
    QPushButton,
    QListWidget,
    QApplication,
    QTableWidget,
    QSizePolicy,
    QHeaderView,
    QDialog,
    QVBoxLayout,
    QLabel,
    QLineEdit,
    QDateEdit,
    QComboBox,
    QTableWidgetItem,
    QMessageBox,
)
from PySide6.QtCore import Qt
from PySide6.QtGui import QIcon
from Ui_main import Ui_Form
from datetime import datetime


channel = grpc.insecure_channel("localhost:8189")
stub = hospital_pb2_grpc.HospitalServiceStub(channel)


class HOS_SYS(QWidget, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.tableWidget_init()
        self.adjustSize()
        self.main_Button.clicked.connect(self.to_main_ui)
        self.Book_Button.clicked.connect(self.Book_)
        self.IDQuery_Button.clicked.connect(self.IDQuery)
        self.NameQuery_Button.clicked.connect(self.NameQuery)
        self.cancel_button.clicked.connect(self.cancelByID)
        # 公用消息框
        self.messageBox = QMessageBox(self)
        # 公用预约列表
        self.appointmentList = hospital_pb2.AppointmentList()

    def tableWidget_init(self):
        self.tableWidget.setColumnCount(6)
        self.tableWidget.setHorizontalHeaderLabels(
            ["ID", "患者姓名", "医生姓名", "科室", "预约日期", "预约时段"]
        )
        # 设置列宽自适应内容
        header = self.tableWidget.horizontalHeader()
        header.setSectionResizeMode(QHeaderView.ResizeToContents)  # 根据内容调整列宽
        header.setSectionResizeMode(5, QHeaderView.Stretch)  # 最后一列填充剩余空间
        # 调整窗口以适应内容
        self.tableWidget.resizeColumnsToContents()
        self.adjustSize()
        self.tableWidget.verticalHeader().setVisible(False)

    def to_main_ui(self):
        self.addRecordingByList(self.appointmentList)

    def Book_(self):
        dialog = AppointmentDialog()
        result = dialog.exec()
        if result == QDialog.Accepted:
            patient_id, patient_name, doctor_name, department, date, time_slot = (
                dialog.get_appointment_info()
            )

            appointment = hospital_pb2.Appointment(
                id=patient_id,
                patient_name=patient_name,
                doctor_name=doctor_name,
                department=department,
                date=date,
                time_slot=time_slot,
            )
            sever_response = stub.BookAppointment(appointment)
            if sever_response.success:
                self.messageBox.setText(sever_response.message)
                self.messageBox.exec()
            else:
                self.messageBox.setText("预约失败!")
                self.messageBox.exec()
                return
            self.addRecording(appointment, True)

    def addRecording(self, appointment: hospital_pb2.Appointment, is_first: bool):
        row_count = self.tableWidget.rowCount()
        self.tableWidget.insertRow(row_count)
        self.tableWidget.setItem(row_count, 0, QTableWidgetItem(str(appointment.id)))
        self.tableWidget.setItem(
            row_count, 1, QTableWidgetItem(appointment.patient_name)
        )
        self.tableWidget.setItem(
            row_count, 2, QTableWidgetItem(appointment.doctor_name)
        )
        self.tableWidget.setItem(row_count, 3, QTableWidgetItem(appointment.department))
        self.tableWidget.setItem(row_count, 4, QTableWidgetItem(appointment.date))
        self.tableWidget.setItem(row_count, 5, QTableWidgetItem(appointment.time_slot))
        # 把预约记录添加到公共预约列表
        if is_first:
            self.appointmentList.appointments.append(appointment)

    def IDQuery(self):
        dialog = IDQueryDialog()
        result = dialog.exec()
        if result == QDialog.Accepted:
            request = hospital_pb2.AppointmentIDRequest(id=dialog.get_ID())
            appointment = stub.QueryByID(request)
            self.tableWidget.setRowCount(0)
            self.addRecording(appointment, False)

    def NameQuery(self):
        dialog = nameQueryDialog()
        result = dialog.exec()
        if result == QDialog.Accepted:
            request = hospital_pb2.PatientRequest(patient_name=dialog.get_name())
            appointmentList = stub.QueryByPatient(request)
            self.tableWidget.setRowCount(0)
            for appointment in appointmentList.appointments:
                self.addRecording(appointment, False)

    def cancelByID(self):
        dialog = CancelByIDDialog()
        result = dialog.exec()
        if result == QDialog.Accepted:
            id_ = dialog.get_ID()
            request = hospital_pb2.AppointmentIDRequest(id=id_)
            response = stub.CancelAppointment(request)
            if response.success:
                self.messageBox.setText("取消预约成功！")
                appointmentList = hospital_pb2.AppointmentList()
                for appointment in self.appointmentList.appointments:
                    if appointment.id != id_:
                        appointmentList.appointments.append(appointment)
                self.appointmentList = appointmentList
                self.addRecordingByList(self.appointmentList)

    def addRecordingByList(self, appointmentList: hospital_pb2.AppointmentList):
        self.tableWidget.setRowCount(0)
        for appointment in appointmentList.appointments:
            row_count = self.tableWidget.rowCount()
            self.tableWidget.insertRow(row_count)
            self.tableWidget.setItem(
                row_count, 0, QTableWidgetItem(str(appointment.id))
            )
            self.tableWidget.setItem(
                row_count, 1, QTableWidgetItem(appointment.patient_name)
            )
            self.tableWidget.setItem(
                row_count, 2, QTableWidgetItem(appointment.doctor_name)
            )
            self.tableWidget.setItem(
                row_count, 3, QTableWidgetItem(appointment.department)
            )
            self.tableWidget.setItem(row_count, 4, QTableWidgetItem(appointment.date))
            self.tableWidget.setItem(
                row_count, 5, QTableWidgetItem(appointment.time_slot)
            )


class AppointmentDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("填写预约信息")
        layout = QVBoxLayout()

        self.patient_id_label = QLabel("患者id:")
        self.patient_id_input = QLineEdit()
        layout.addWidget(self.patient_id_label)
        layout.addWidget(self.patient_id_input)

        # 患者姓名
        self.patient_name_label = QLabel("患者姓名:")
        self.patient_name_input = QLineEdit()
        layout.addWidget(self.patient_name_label)
        layout.addWidget(self.patient_name_input)

        # 医生姓名
        self.doctor_name_label = QLabel("医生姓名:")
        self.doctor_name_input = QLineEdit()
        layout.addWidget(self.doctor_name_label)
        layout.addWidget(self.doctor_name_input)

        # 科室
        self.department_label = QLabel("科室:")
        self.department_combo = QComboBox()
        self.department_combo.addItems(["内科", "外科", "眼科", "牙科"])
        layout.addWidget(self.department_label)
        layout.addWidget(self.department_combo)

        # 预约日期
        self.date_label = QLabel("预约日期:")
        self.date_edit = QDateEdit()
        self.date_edit.setDate(datetime.now().date())
        layout.addWidget(self.date_label)
        layout.addWidget(self.date_edit)

        # 预约时段
        self.time_label = QLabel("预约时段:")
        self.time_combo = QComboBox()
        self.time_combo.addItems(["10:00-11:00", "14:00-15:00", "16:00-17:00"])
        layout.addWidget(self.time_label)
        layout.addWidget(self.time_combo)

        # 确定按钮
        self.confirm_button = QPushButton("确定")
        self.confirm_button.clicked.connect(self.accept)
        layout.addWidget(self.confirm_button)

        self.setLayout(layout)

    def get_appointment_info(self):
        patient_id = int(self.patient_id_input.text())
        patient_name = self.patient_name_input.text()
        doctor_name = self.doctor_name_input.text()
        department = self.department_combo.currentText()
        date = self.date_edit.date().toString("yyyy-MM-dd")
        time_slot = self.time_combo.currentText()
        return patient_id, patient_name, doctor_name, department, date, time_slot


class IDQueryDialog(QDialog):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout()
        self.setWindowTitle("根据ID查询信息")
        self.ID_label = QLabel("ID:")
        self.ID_input = QLineEdit()
        layout.addWidget(self.ID_label)
        layout.addWidget(self.ID_input)
        self.confirm_button = QPushButton("确定")
        self.confirm_button.clicked.connect(self.accept)
        layout.addWidget(self.confirm_button)
        self.setLayout(layout)

    def get_ID(self):
        return int(self.ID_input.text())


class nameQueryDialog(QDialog):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout()
        self.setWindowTitle("根据姓名查询信息")
        self.Name_label = QLabel("name:")
        self.Name_input = QLineEdit()
        layout.addWidget(self.Name_label)
        layout.addWidget(self.Name_input)
        self.confirm_button = QPushButton("确定")
        self.confirm_button.clicked.connect(self.accept)
        layout.addWidget(self.confirm_button)
        self.setLayout(layout)

    def get_name(self):
        return self.Name_input.text()


class CancelByIDDialog(QDialog):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout()
        self.setWindowTitle("根据ID删除信息")
        self.ID_label = QLabel("ID:")
        self.ID_input = QLineEdit()
        layout.addWidget(self.ID_label)
        layout.addWidget(self.ID_input)
        self.confirm_button = QPushButton("确定")
        self.confirm_button.clicked.connect(self.accept)
        layout.addWidget(self.confirm_button)
        self.setLayout(layout)

    def get_ID(self):
        return int(self.ID_input.text())


if __name__ == "__main__":
    app = QApplication([])
    hos_sys = HOS_SYS()
    hos_sys.show()
    app.exec()
