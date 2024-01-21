#!/usr/bin/env python3

import os
import subprocess
import sys
try:
    import reportlab
except ModuleNotFoundError:
    subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'reportlab'])
    import reportlab
from reportlab.platypus import SimpleDocTemplate
from reportlab.platypus import Paragraph, Spacer, Table
from reportlab.lib.styles import getSampleStyleSheet

def generate_report(filePath, title, content):
    styles = getSampleStyleSheet()
    report = SimpleDocTemplate(filePath)
    reportTitle = Paragraph(title, styles["h1"])
    reportContent = Paragraph(content, styles["BodyText"])
    spacerLine = Spacer(1,20)
    report.build([reportTitle, spacerLine, reportContent])
    