# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: egm.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\tegm.proto\x12\x07\x61\x62\x62.egm\"\xeb\x01\n\tEgmHeader\x12\r\n\x05seqno\x18\x01 \x01(\r\x12\n\n\x02tm\x18\x02 \x01(\r\x12@\n\x05mtype\x18\x03 \x01(\x0e\x32\x1e.abb.egm.EgmHeader.MessageType:\x11MSGTYPE_UNDEFINED\"\x80\x01\n\x0bMessageType\x12\x15\n\x11MSGTYPE_UNDEFINED\x10\x00\x12\x13\n\x0fMSGTYPE_COMMAND\x10\x01\x12\x10\n\x0cMSGTYPE_DATA\x10\x02\x12\x16\n\x12MSGTYPE_CORRECTION\x10\x03\x12\x1b\n\x17MSGTYPE_PATH_CORRECTION\x10\x04\"/\n\x0c\x45gmCartesian\x12\t\n\x01x\x18\x01 \x02(\x01\x12\t\n\x01y\x18\x02 \x02(\x01\x12\t\n\x01z\x18\x03 \x02(\x01\"?\n\rEgmQuaternion\x12\n\n\x02u0\x18\x01 \x02(\x01\x12\n\n\x02u1\x18\x02 \x02(\x01\x12\n\n\x02u2\x18\x03 \x02(\x01\x12\n\n\x02u3\x18\x04 \x02(\x01\"+\n\x08\x45gmEuler\x12\t\n\x01x\x18\x01 \x02(\x01\x12\t\n\x01y\x18\x02 \x02(\x01\x12\t\n\x01z\x18\x03 \x02(\x01\"w\n\x07\x45gmPose\x12\"\n\x03pos\x18\x01 \x01(\x0b\x32\x15.abb.egm.EgmCartesian\x12&\n\x06orient\x18\x02 \x01(\x0b\x32\x16.abb.egm.EgmQuaternion\x12 \n\x05\x65uler\x18\x03 \x01(\x0b\x32\x11.abb.egm.EgmEuler\"\"\n\x11\x45gmCartesianSpeed\x12\r\n\x05value\x18\x01 \x03(\x01\"\x1b\n\tEgmJoints\x12\x0e\n\x06joints\x18\x01 \x03(\x01\"#\n\x11\x45gmExternalJoints\x12\x0e\n\x06joints\x18\x01 \x03(\x01\"\x81\x01\n\nEgmPlanned\x12\"\n\x06joints\x18\x01 \x01(\x0b\x32\x12.abb.egm.EgmJoints\x12#\n\tcartesian\x18\x02 \x01(\x0b\x32\x10.abb.egm.EgmPose\x12*\n\x0e\x65xternalJoints\x18\x03 \x01(\x0b\x32\x12.abb.egm.EgmJoints\"\x8d\x01\n\x0b\x45gmSpeedRef\x12\"\n\x06joints\x18\x01 \x01(\x0b\x32\x12.abb.egm.EgmJoints\x12.\n\ncartesians\x18\x02 \x01(\x0b\x32\x1a.abb.egm.EgmCartesianSpeed\x12*\n\x0e\x65xternalJoints\x18\x03 \x01(\x0b\x32\x12.abb.egm.EgmJoints\">\n\x0b\x45gmPathCorr\x12\"\n\x03pos\x18\x01 \x02(\x0b\x32\x15.abb.egm.EgmCartesian\x12\x0b\n\x03\x61ge\x18\x02 \x02(\r\"\x82\x01\n\x0b\x45gmFeedBack\x12\"\n\x06joints\x18\x01 \x01(\x0b\x32\x12.abb.egm.EgmJoints\x12#\n\tcartesian\x18\x02 \x01(\x0b\x32\x10.abb.egm.EgmPose\x12*\n\x0e\x65xternalJoints\x18\x03 \x01(\x0b\x32\x12.abb.egm.EgmJoints\"\x8c\x01\n\rEgmMotorState\x12\x34\n\x05state\x18\x01 \x02(\x0e\x32%.abb.egm.EgmMotorState.MotorStateType\"E\n\x0eMotorStateType\x12\x14\n\x10MOTORS_UNDEFINED\x10\x00\x12\r\n\tMOTORS_ON\x10\x01\x12\x0e\n\nMOTORS_OFF\x10\x02\"\xa2\x01\n\x0b\x45gmMCIState\x12?\n\x05state\x18\x01 \x02(\x0e\x32!.abb.egm.EgmMCIState.MCIStateType:\rMCI_UNDEFINED\"R\n\x0cMCIStateType\x12\x11\n\rMCI_UNDEFINED\x10\x00\x12\r\n\tMCI_ERROR\x10\x01\x12\x0f\n\x0bMCI_STOPPED\x10\x02\x12\x0f\n\x0bMCI_RUNNING\x10\x03\"\xc3\x01\n\x15\x45gmRapidCtrlExecState\x12U\n\x05state\x18\x01 \x02(\x0e\x32\x35.abb.egm.EgmRapidCtrlExecState.RapidCtrlExecStateType:\x0fRAPID_UNDEFINED\"S\n\x16RapidCtrlExecStateType\x12\x13\n\x0fRAPID_UNDEFINED\x10\x00\x12\x11\n\rRAPID_STOPPED\x10\x01\x12\x11\n\rRAPID_RUNNING\x10\x02\"!\n\x0e\x45gmTestSignals\x12\x0f\n\x07signals\x18\x01 \x03(\x01\"\xd1\x02\n\x08\x45gmRobot\x12\"\n\x06header\x18\x01 \x01(\x0b\x32\x12.abb.egm.EgmHeader\x12&\n\x08\x66\x65\x65\x64\x42\x61\x63k\x18\x02 \x01(\x0b\x32\x14.abb.egm.EgmFeedBack\x12$\n\x07planned\x18\x03 \x01(\x0b\x32\x13.abb.egm.EgmPlanned\x12*\n\nmotorState\x18\x04 \x01(\x0b\x32\x16.abb.egm.EgmMotorState\x12&\n\x08mciState\x18\x05 \x01(\x0b\x32\x14.abb.egm.EgmMCIState\x12\x19\n\x11mciConvergenceMet\x18\x06 \x01(\x08\x12,\n\x0btestSignals\x18\x07 \x01(\x0b\x32\x17.abb.egm.EgmTestSignals\x12\x36\n\x0erapidExecState\x18\x08 \x01(\x0b\x32\x1e.abb.egm.EgmRapidCtrlExecState\"}\n\tEgmSensor\x12\"\n\x06header\x18\x01 \x01(\x0b\x32\x12.abb.egm.EgmHeader\x12$\n\x07planned\x18\x02 \x01(\x0b\x32\x13.abb.egm.EgmPlanned\x12&\n\x08speedRef\x18\x03 \x01(\x0b\x32\x14.abb.egm.EgmSpeedRef\"_\n\x11\x45gmSensorPathCorr\x12\"\n\x06header\x18\x01 \x01(\x0b\x32\x12.abb.egm.EgmHeader\x12&\n\x08pathCorr\x18\x02 \x01(\x0b\x32\x14.abb.egm.EgmPathCorr')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'egm_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _EGMHEADER._serialized_start=23
  _EGMHEADER._serialized_end=258
  _EGMHEADER_MESSAGETYPE._serialized_start=130
  _EGMHEADER_MESSAGETYPE._serialized_end=258
  _EGMCARTESIAN._serialized_start=260
  _EGMCARTESIAN._serialized_end=307
  _EGMQUATERNION._serialized_start=309
  _EGMQUATERNION._serialized_end=372
  _EGMEULER._serialized_start=374
  _EGMEULER._serialized_end=417
  _EGMPOSE._serialized_start=419
  _EGMPOSE._serialized_end=538
  _EGMCARTESIANSPEED._serialized_start=540
  _EGMCARTESIANSPEED._serialized_end=574
  _EGMJOINTS._serialized_start=576
  _EGMJOINTS._serialized_end=603
  _EGMEXTERNALJOINTS._serialized_start=605
  _EGMEXTERNALJOINTS._serialized_end=640
  _EGMPLANNED._serialized_start=643
  _EGMPLANNED._serialized_end=772
  _EGMSPEEDREF._serialized_start=775
  _EGMSPEEDREF._serialized_end=916
  _EGMPATHCORR._serialized_start=918
  _EGMPATHCORR._serialized_end=980
  _EGMFEEDBACK._serialized_start=983
  _EGMFEEDBACK._serialized_end=1113
  _EGMMOTORSTATE._serialized_start=1116
  _EGMMOTORSTATE._serialized_end=1256
  _EGMMOTORSTATE_MOTORSTATETYPE._serialized_start=1187
  _EGMMOTORSTATE_MOTORSTATETYPE._serialized_end=1256
  _EGMMCISTATE._serialized_start=1259
  _EGMMCISTATE._serialized_end=1421
  _EGMMCISTATE_MCISTATETYPE._serialized_start=1339
  _EGMMCISTATE_MCISTATETYPE._serialized_end=1421
  _EGMRAPIDCTRLEXECSTATE._serialized_start=1424
  _EGMRAPIDCTRLEXECSTATE._serialized_end=1619
  _EGMRAPIDCTRLEXECSTATE_RAPIDCTRLEXECSTATETYPE._serialized_start=1536
  _EGMRAPIDCTRLEXECSTATE_RAPIDCTRLEXECSTATETYPE._serialized_end=1619
  _EGMTESTSIGNALS._serialized_start=1621
  _EGMTESTSIGNALS._serialized_end=1654
  _EGMROBOT._serialized_start=1657
  _EGMROBOT._serialized_end=1994
  _EGMSENSOR._serialized_start=1996
  _EGMSENSOR._serialized_end=2121
  _EGMSENSORPATHCORR._serialized_start=2123
  _EGMSENSORPATHCORR._serialized_end=2218
# @@protoc_insertion_point(module_scope)
