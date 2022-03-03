import os

reportFolder="Report"

screenshotReportFolder=reportFolder+"\\"+"Screenshot"

os.mkdir(screenshotReportFolder)
excelReportFolder=reportFolder+"\\"+'Excel'

if not reportFolder:
    os.mkdir(reportFolder)

if not screenshotReportFolder:
    os.mkdir(screenshotReportFolder)


if not excelReportFolder:
    os.mkdir(excelReportFolder)
