from dataclasses import dataclass
import logging
import os

from .savefile import SaveFile
import mobase # pyright: ignore[reportMissingModuleSource]
from PyQt6.QtCore import QCoreApplication # type: ignore
from PyQt6.QtGui import QIcon # type: ignore
from PyQt6.QtWidgets import QMessageBox, QDialog, QDialogButtonBox, QFileDialog # type: ignore

logger = logging.getLogger('CNSSaveConverter_Plugin')

@dataclass
class Args:
  indent: int = 2

class Plugin(mobase.IPluginTool):
  def init(self, organizer):
    self.__organizer = organizer
    self.__args = Args(indent=self.pluginSetting("indent"))
    return True

  def name(self):
    return "CNS save file JSON converter"

  def displayName(self):
    return self.name()

  def author(self):
    return "github.com/lotress"

  def description(self):
    return self.tr("A tool convert CNS save file from/to JSON file.")

  def tooltip(self):
    return self.description()

  def version(self):
    return mobase.VersionInfo(1, 0, 0, 0)

  def isActive(self):
    return True

  def pluginSetting(self, name):
    return self.__organizer.pluginSetting(self.name(), name)

  def setPluginSetting(self, name, value):
    self.__organizer.setPluginSetting(self.name(), name, value)

  def settings(self):
    return [mobase.PluginSetting('indent', self.tr('JSON indent level.'), 2)]

  def icon(self):
    return QIcon()

  def setParentWidget(self, widget):
    self.__parentWidget = widget

  def tr(self, str):
    return QCoreApplication.translate("CNSSaveConverter", str)

  def display(self):
    self.__args.indent = self.pluginSetting('indent')
    saveDirectory = self.__organizer.managedGame().savesDirectory().absolutePath()
    parent = getattr(self, '_Plugin__parentWidget', None)

    # Ask user to pick an input file (.sav or .json)
    caption = self.tr('Open save or JSON file')
    file_filter = self.tr('CNS Save or JSON Files (*.sav *.json);;All files (*)')
    input_path, _ = QFileDialog.getOpenFileName(parent, caption, saveDirectory, file_filter)
    if not input_path:
      return

    try:
      base, ext = os.path.splitext(input_path)
      ext = ext.lower()
      # Suggest output filename
      if ext == '.sav':
        suggested = base + '.json'
      elif ext == '.json':
        suggested = base + '.sav'
      else:
        # if unknown, default to .json
        suggested = base + '.json'

      out_caption = self.tr('Save converted file as')
      out_filter = self.tr('{};;All files (*)'.format('CNS Save Files (*.sav)' if ext == '.json' else 'JSON files (*.json)'))
      output_path, _ = QFileDialog.getSaveFileName(parent, out_caption, suggested, out_filter)
      if not output_path:
        return

      if ext == '.sav':
        save = SaveFile.loadSave(input_path)
        save.dumpJson(output_path, indent=self.__args.indent)
        msg = self.tr('Converted save file to JSON: {0}').format(output_path)
      else:
        save = SaveFile.loadJson(input_path)
        save.dumpSave(output_path)
        msg = self.tr('Converted JSON to save file: {0}').format(output_path)

      logger.info(msg)
      QMessageBox.information(parent, self.name(), msg)
    except Exception as e:
      logger.exception('Conversion failed')
      QMessageBox.critical(parent, self.tr('Error'), str(e))

createPlugin = Plugin