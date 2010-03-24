# -*- coding: utf-8 -*-
# user-settings.py - custom Orca settings
# Generated by orca.  DO NOT EDIT THIS FILE!!!
# If you want permanent customizations that will not
# be overwritten, edit orca-customizations.py.
#
import re
import time

import orca.debug
import orca.settings
import orca.acss

#orca.debug.debugLevel = orca.debug.LEVEL_OFF
orca.debug.debugLevel = orca.debug.LEVEL_SEVERE
#orca.debug.debugLevel = orca.debug.LEVEL_WARNING
#orca.debug.debugLevel = orca.debug.LEVEL_INFO
#orca.debug.debugLevel = orca.debug.LEVEL_CONFIGURATION
#orca.debug.debugLevel = orca.debug.LEVEL_FINE
#orca.debug.debugLevel = orca.debug.LEVEL_FINER
#orca.debug.debugLevel = orca.debug.LEVEL_FINEST
#orca.debug.debugLevel = orca.debug.LEVEL_ALL

#orca.debug.eventDebugLevel = orca.debug.LEVEL_OFF
#orca.debug.eventDebugFilter = None
#orca.debug.eventDebugFilter = re.compile('[\S]*focus|[\S]*activ')
#orca.debug.eventDebugFilter = re.compile('nomatch')
#orca.debug.eventDebugFilter = re.compile('[\S]*:accessible-name')
#orca.debug.eventDebugFilter = re.compile('[\S]*:(?!bounds-changed)')

#orca.debug.debugFile = open(time.strftime('debug-%Y-%m-%d-%H:%M:%S.out'), 'w', 0)
#orca.debug.debugFile = open('debug.out', 'w', 0)

#orca.settings.useBonoboMain=False
#orca.settings.debugEventQueue=True
#orca.settings.gilSleepTime=0

if False:
    import sys
    import orca.debug
    sys.settrace(orca.debug.traceit)
    orca.debug.debugLevel = orca.debug.LEVEL_ALL

orca.settings.orcaModifierKeys = orca.settings.LAPTOP_MODIFIER_KEYS
orca.settings.enableSpeech = True
orca.settings.speechServerFactory = 'orca.speechdispatcherfactory'
orca.settings.speechServerInfo = ['Default Synthesizer', 'default']
orca.settings.voices = {
'default' : orca.acss.ACSS({'average-pitch': 5.0, 'gain': 10.0, 'rate': 60.0}),
'uppercase' : orca.acss.ACSS({'average-pitch': 5.5999999999999996}),
'hyperlink' : orca.acss.ACSS({}),
}
orca.settings.speechVerbosityLevel = orca.settings.VERBOSITY_LEVEL_VERBOSE
orca.settings.readTableCellRow = True
orca.settings.enableSpeechIndentation = False
orca.settings.enableEchoByCharacter = False
orca.settings.enableEchoByWord = False
orca.settings.enableEchoBySentence = False
orca.settings.enableKeyEcho = True
orca.settings.enablePrintableKeys = True
orca.settings.enableModifierKeys = True
orca.settings.enableLockingKeys = True
orca.settings.enableFunctionKeys = True
orca.settings.enableActionKeys = True
orca.settings.enableNavigationKeys = False
orca.settings.enableDiacriticalKeys = False
orca.settings.enablePauseBreaks = True
orca.settings.enableTutorialMessages = False
orca.settings.enableMnemonicSpeaking = False
orca.settings.enablePositionSpeaking = False
orca.settings.enableBraille = True
orca.settings.enableBrailleContext = True
orca.settings.enableBrailleGrouping = False
orca.settings.disableBrailleEOL = False
orca.settings.brailleEOLIndicator = ' $l'
orca.settings.brailleVerbosityLevel = orca.settings.VERBOSITY_LEVEL_VERBOSE
orca.settings.brailleRolenameStyle = orca.settings.BRAILLE_ROLENAME_STYLE_LONG
orca.settings.brailleSelectorIndicator = orca.settings.BRAILLE_SEL_BOTH
orca.settings.brailleLinkIndicator = orca.settings.BRAILLE_LINK_BOTH
orca.settings.brailleAlignmentStyle = orca.settings.ALIGN_BRAILLE_BY_EDGE
orca.settings.enableBrailleMonitor = False
orca.settings.enableMagnifier = False
orca.settings.enableMagLiveUpdating = True
orca.settings.enableMagCursor = True
orca.settings.enableMagCursorExplicitSize = False
orca.settings.magHideCursor = True
orca.settings.magCursorSize = 32
orca.settings.magCursorColor = '#000000'
orca.settings.enableMagCrossHair = True
orca.settings.enableMagCrossHairClip = False
orca.settings.magCrossHairSize = 16
orca.settings.magCrossHairColor = '#000000'
orca.settings.magZoomerType = orca.settings.MAG_ZOOMER_TYPE_FULL_SCREEN
orca.settings.magZoomerLeft = 400
orca.settings.magZoomerRight = 800
orca.settings.magZoomerTop = 0
orca.settings.magZoomerBottom = 600
orca.settings.magZoomFactor = 4.0
orca.settings.enableMagZoomerBorder = False
orca.settings.magZoomerBorderSize = 1
orca.settings.magZoomerBorderColor = '#000000'
orca.settings.enableMagZoomerColorInversion = True
orca.settings.magBrightnessLevel = 0
orca.settings.magBrightnessLevelRed = 0
orca.settings.magBrightnessLevelBlue = 0
orca.settings.magBrightnessLevelGreen = 0
orca.settings.magContrastLevel = 0
orca.settings.magContrastLevelRed = 0
orca.settings.magContrastLevelGreen = 0
orca.settings.magContrastLevelBlue = 0
orca.settings.magSmoothingMode = orca.settings.MAG_SMOOTHING_MODE_BILINEAR
orca.settings.magMouseTrackingMode = orca.settings.MAG_TRACKING_MODE_CENTERED
orca.settings.magControlTrackingMode = orca.settings.MAG_TRACKING_MODE_PUSH
orca.settings.magTextTrackingMode = orca.settings.MAG_TRACKING_MODE_PUSH
orca.settings.magEdgeMargin = 0
orca.settings.magPointerFollowsFocus = False
orca.settings.magPointerFollowsZoomer = True
orca.settings.magColorFilteringMode = orca.settings.MAG_COLOR_FILTERING_MODE_NONE
orca.settings.magSourceDisplay = ':0.0'
orca.settings.magTargetDisplay = ':0.0'
orca.settings.verbalizePunctuationStyle = orca.settings.PUNCTUATION_STYLE_MOST
orca.settings.showMainWindow = True
orca.settings.quitOrcaNoConfirmation = False
orca.settings.presentToolTips = False
orca.settings.sayAllStyle = orca.settings.SAYALL_STYLE_SENTENCE
orca.settings.keyboardLayout = orca.settings.GENERAL_KEYBOARD_LAYOUT_LAPTOP
orca.settings.speakBlankLines = True
orca.settings.speakMultiCaseStringsAsWords = False
orca.settings.enabledSpokenTextAttributes = "size:; family-name:; weight:400; indent:0; underline:none; strikethrough:false; justification:left; style:normal; paragraph-style:;"
orca.settings.enabledBrailledTextAttributes = "size:; family-name:; weight:400; indent:0; underline:none; strikethrough:false; justification:left; style:normal;"
orca.settings.textAttributesBrailleIndicator = orca.settings.TEXT_ATTR_BRAILLE_NONE
orca.settings.enableProgressBarUpdates = True
orca.settings.progressBarUpdateInterval = 10
orca.settings.progressBarVerbosity = orca.settings.PROGRESS_BAR_APPLICATION
orca.settings.enableContractedBraille = False
orca.settings.brailleContractionTable = '/usr/share/liblouis/tables/en-us-comp6.ctb'
orca.settings.enableMouseReview = False
orca.settings.mouseDwellDelay = 0
orca.settings.speakCellCoordinates = True
orca.settings.speakCellSpan = True
orca.settings.speakCellHeaders = True
orca.settings.skipBlankCells = False
orca.settings.largeObjectTextLength = 75
orca.settings.wrappedStructuralNavigation = True
orca.settings.presentRequiredState = False
orca.settings.brailleRequiredStateString = 'required'
orca.settings.speechRequiredStateString = 'required'

# Set up a user key-bindings profile
#
def overrideKeyBindings(script, keyB):
   keyB.removeByHandler(script.inputEventHandlers['decreaseSpeechRateHandler'])
   keyB.add(orca.keybindings.KeyBinding(
      'Down',
      365,
      256,
      script.inputEventHandlers["decreaseSpeechRateHandler"]))

   keyB.removeByHandler(script.inputEventHandlers['increaseMagnificationHandler'])
   keyB.add(orca.keybindings.KeyBinding(
      'equal',
      365,
      256,
      script.inputEventHandlers["increaseMagnificationHandler"]))

   keyB.removeByHandler(script.inputEventHandlers['toggleMagnifierHandler'])
   keyB.add(orca.keybindings.KeyBinding(
      'g',
      365,
      256,
      script.inputEventHandlers["toggleMagnifierHandler"]))

   keyB.removeByHandler(script.inputEventHandlers['decreaseMagnificationHandler'])
   keyB.add(orca.keybindings.KeyBinding(
      'minus',
      365,
      256,
      script.inputEventHandlers["decreaseMagnificationHandler"]))

   keyB.removeByHandler(script.inputEventHandlers['increaseSpeechRateHandler'])
   keyB.add(orca.keybindings.KeyBinding(
      'Up',
      365,
      256,
      script.inputEventHandlers["increaseSpeechRateHandler"]))

   keyB.removeByHandler(script.inputEventHandlers['toggleMouseEnhancementsHandler'])
   keyB.add(orca.keybindings.KeyBinding(
      'x',
      365,
      256,
      script.inputEventHandlers["toggleMouseEnhancementsHandler"]))

   keyB.removeByHandler(script.inputEventHandlers['toggleColorEnhancementsHandler'])
   keyB.add(orca.keybindings.KeyBinding(
      'n',
      365,
      256,
      script.inputEventHandlers["toggleColorEnhancementsHandler"]))

   keyB.removeByHandler(script.inputEventHandlers['increaseSpeechPitchHandler'])
   keyB.add(orca.keybindings.KeyBinding(
      'period',
      365,
      257,
      script.inputEventHandlers["increaseSpeechPitchHandler"]))

   keyB.removeByHandler(script.inputEventHandlers['decreaseSpeechPitchHandler'])
   keyB.add(orca.keybindings.KeyBinding(
      'comma',
      365,
      257,
      script.inputEventHandlers["decreaseSpeechPitchHandler"]))

   return keyB

orca.settings.overrideKeyBindings = overrideKeyBindings

# User customized pronunciation dictionary settings
#
import orca.pronunciation_dict

orca.pronunciation_dict.pronunciation_dict={}

import orca.orca_state

try:
    reload(orca.orca_state.orcaCustomizations)
except AttributeError:
    try:
        orca.orca_state.orcaCustomizations = __import__("orca-customizations")
    except ImportError:
        pass
