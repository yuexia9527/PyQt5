/********************************************************************************
** Form generated from reading UI file 'MainWindow.ui'
**
** Created by: Qt User Interface Compiler version 5.10.1
**
** WARNING! All changes made in this file will be lost when recompiling UI file!
********************************************************************************/

#ifndef UI_MAINWINDOW_H
#define UI_MAINWINDOW_H

#include <QtCore/QVariant>
#include <QtWidgets/QAction>
#include <QtWidgets/QApplication>
#include <QtWidgets/QButtonGroup>
#include <QtWidgets/QHeaderView>
#include <QtWidgets/QMainWindow>
#include <QtWidgets/QMenuBar>
#include <QtWidgets/QStatusBar>
#include <QtWidgets/QTableView>
#include <QtWidgets/QToolBar>
#include <QtWidgets/QWidget>

QT_BEGIN_NAMESPACE

class Ui_MainWindow
{
public:
    QAction *actOpenDB;
    QAction *actQuit;
    QAction *actRecInsert;
    QAction *actRecDelete;
    QAction *actRecEdit;
    QAction *actScan;
    QAction *actTestSQL;
    QWidget *centralWidget;
    QTableView *tableView;
    QMenuBar *menuBar;
    QStatusBar *statusBar;
    QToolBar *mainToolBar;

    void setupUi(QMainWindow *MainWindow)
    {
        if (MainWindow->objectName().isEmpty())
            MainWindow->setObjectName(QStringLiteral("MainWindow"));
        MainWindow->resize(631, 385);
        QFont font;
        font.setPointSize(11);
        MainWindow->setFont(font);
        actOpenDB = new QAction(MainWindow);
        actOpenDB->setObjectName(QStringLiteral("actOpenDB"));
        QIcon icon;
        icon.addFile(QStringLiteral(":/icons/images/open3.bmp"), QSize(), QIcon::Normal, QIcon::Off);
        actOpenDB->setIcon(icon);
        actQuit = new QAction(MainWindow);
        actQuit->setObjectName(QStringLiteral("actQuit"));
        QIcon icon1;
        icon1.addFile(QStringLiteral(":/icons/images/exit.bmp"), QSize(), QIcon::Normal, QIcon::Off);
        actQuit->setIcon(icon1);
        actRecInsert = new QAction(MainWindow);
        actRecInsert->setObjectName(QStringLiteral("actRecInsert"));
        actRecInsert->setEnabled(false);
        QIcon icon2;
        icon2.addFile(QStringLiteral(":/icons/images/306.bmp"), QSize(), QIcon::Normal, QIcon::Off);
        actRecInsert->setIcon(icon2);
        actRecDelete = new QAction(MainWindow);
        actRecDelete->setObjectName(QStringLiteral("actRecDelete"));
        actRecDelete->setEnabled(false);
        QIcon icon3;
        icon3.addFile(QStringLiteral(":/icons/images/delete1.bmp"), QSize(), QIcon::Normal, QIcon::Off);
        actRecDelete->setIcon(icon3);
        actRecEdit = new QAction(MainWindow);
        actRecEdit->setObjectName(QStringLiteral("actRecEdit"));
        actRecEdit->setEnabled(false);
        QIcon icon4;
        icon4.addFile(QStringLiteral(":/icons/images/812.bmp"), QSize(), QIcon::Normal, QIcon::Off);
        actRecEdit->setIcon(icon4);
        actScan = new QAction(MainWindow);
        actScan->setObjectName(QStringLiteral("actScan"));
        actScan->setEnabled(false);
        QIcon icon5;
        icon5.addFile(QStringLiteral(":/icons/images/up.bmp"), QSize(), QIcon::Normal, QIcon::Off);
        actScan->setIcon(icon5);
        actTestSQL = new QAction(MainWindow);
        actTestSQL->setObjectName(QStringLiteral("actTestSQL"));
        actTestSQL->setEnabled(false);
        QIcon icon6;
        icon6.addFile(QStringLiteral(":/icons/images/828.bmp"), QSize(), QIcon::Normal, QIcon::Off);
        actTestSQL->setIcon(icon6);
        centralWidget = new QWidget(MainWindow);
        centralWidget->setObjectName(QStringLiteral("centralWidget"));
        tableView = new QTableView(centralWidget);
        tableView->setObjectName(QStringLiteral("tableView"));
        tableView->setGeometry(QRect(95, 20, 431, 241));
        tableView->setSelectionMode(QAbstractItemView::SingleSelection);
        tableView->setSelectionBehavior(QAbstractItemView::SelectRows);
        MainWindow->setCentralWidget(centralWidget);
        menuBar = new QMenuBar(MainWindow);
        menuBar->setObjectName(QStringLiteral("menuBar"));
        menuBar->setGeometry(QRect(0, 0, 631, 23));
        MainWindow->setMenuBar(menuBar);
        statusBar = new QStatusBar(MainWindow);
        statusBar->setObjectName(QStringLiteral("statusBar"));
        MainWindow->setStatusBar(statusBar);
        mainToolBar = new QToolBar(MainWindow);
        mainToolBar->setObjectName(QStringLiteral("mainToolBar"));
        mainToolBar->setToolButtonStyle(Qt::ToolButtonTextUnderIcon);
        MainWindow->addToolBar(Qt::TopToolBarArea, mainToolBar);

        mainToolBar->addAction(actOpenDB);
        mainToolBar->addSeparator();
        mainToolBar->addAction(actRecInsert);
        mainToolBar->addAction(actRecEdit);
        mainToolBar->addAction(actRecDelete);
        mainToolBar->addAction(actScan);
        mainToolBar->addSeparator();
        mainToolBar->addAction(actTestSQL);
        mainToolBar->addAction(actQuit);

        retranslateUi(MainWindow);
        QObject::connect(actQuit, SIGNAL(triggered()), MainWindow, SLOT(close()));

        QMetaObject::connectSlotsByName(MainWindow);
    } // setupUi

    void retranslateUi(QMainWindow *MainWindow)
    {
        MainWindow->setWindowTitle(QApplication::translate("MainWindow", "Demo7_3, QSqlQuery\347\232\204\344\275\277\347\224\250", nullptr));
        actOpenDB->setText(QApplication::translate("MainWindow", "\346\211\223\345\274\200\346\225\260\346\215\256\345\272\223", nullptr));
#ifndef QT_NO_TOOLTIP
        actOpenDB->setToolTip(QApplication::translate("MainWindow", "\346\211\223\345\274\200\346\225\260\346\215\256\345\272\223", nullptr));
#endif // QT_NO_TOOLTIP
        actQuit->setText(QApplication::translate("MainWindow", "\351\200\200\345\207\272", nullptr));
#ifndef QT_NO_TOOLTIP
        actQuit->setToolTip(QApplication::translate("MainWindow", "\351\200\200\345\207\272", nullptr));
#endif // QT_NO_TOOLTIP
        actRecInsert->setText(QApplication::translate("MainWindow", "\346\217\222\345\205\245\350\256\260\345\275\225", nullptr));
#ifndef QT_NO_TOOLTIP
        actRecInsert->setToolTip(QApplication::translate("MainWindow", "\346\217\222\345\205\245\350\256\260\345\275\225", nullptr));
#endif // QT_NO_TOOLTIP
        actRecDelete->setText(QApplication::translate("MainWindow", "\345\210\240\351\231\244\350\256\260\345\275\225", nullptr));
#ifndef QT_NO_TOOLTIP
        actRecDelete->setToolTip(QApplication::translate("MainWindow", "\345\210\240\351\231\244\350\256\260\345\275\225", nullptr));
#endif // QT_NO_TOOLTIP
        actRecEdit->setText(QApplication::translate("MainWindow", "\347\274\226\350\276\221\350\256\260\345\275\225", nullptr));
#ifndef QT_NO_TOOLTIP
        actRecEdit->setToolTip(QApplication::translate("MainWindow", "\347\274\226\350\276\221\350\256\260\345\275\225", nullptr));
#endif // QT_NO_TOOLTIP
        actScan->setText(QApplication::translate("MainWindow", "\346\266\250\345\267\245\350\265\204", nullptr));
#ifndef QT_NO_TOOLTIP
        actScan->setToolTip(QApplication::translate("MainWindow", "\346\266\250\345\267\245\350\265\204", nullptr));
#endif // QT_NO_TOOLTIP
        actTestSQL->setText(QApplication::translate("MainWindow", "SQL\346\265\213\350\257\225", nullptr));
#ifndef QT_NO_TOOLTIP
        actTestSQL->setToolTip(QApplication::translate("MainWindow", "SQL\350\257\255\345\217\245\346\265\213\350\257\225", nullptr));
#endif // QT_NO_TOOLTIP
    } // retranslateUi

};

namespace Ui {
    class MainWindow: public Ui_MainWindow {};
} // namespace Ui

QT_END_NAMESPACE

#endif // UI_MAINWINDOW_H
