#!/usr/bin/env python

import idmefv2_pb2

import datetime
import hashlib
import json
import uuid
from google.protobuf import timestamp_pb2
from google.protobuf.json_format import MessageToJson


idmef = idmefv2_pb2.IDMEF()

# Root attributes
# Listed attributes -> append or extend directly
# Timestamp -> use the Timestamp object (GetCurrentTime actually is setting the value)
idmef.Version = "2.0.3"
idmef.ID = str(uuid.uuid4())
idmef.Category.append(idmefv2_pb2.IDMEF.CategoryEnum.Category_Test_Test)
idmef.Cause = idmefv2_pb2.IDMEF.CauseEnum.Cause_Error
idmef.Description = "Test message"
idmef.Status = idmefv2_pb2.IDMEF.StatusEnum.Status_Event
idmef.Severity = idmefv2_pb2.IDMEF.SeverityEnum.Severity_Low
idmef.Confidence = 0.5
idmef.Note = "Still a test message"
idmef.CreateTime.GetCurrentTime()
idmef.StartTime.FromDatetime(datetime.datetime.strptime("15/11/2021 09:00", "%d/%m/%Y %H:%M"))
idmef.CeaseTime.FromDatetime(datetime.datetime.strptime("30/11/2021 15:35", "%d/%m/%Y %H:%M"))
idmef.DeleteTime.FromDatetime(datetime.datetime.strptime("30/11/2021 16:00", "%d/%m/%Y %H:%M"))
idmef.AltNames.extend(["Test", "Tests", "Test1"])
idmef.AltCategory.extend(["Cat1", "Cat2", "Cat3"])
idmef.Ref.extend(["Ref-001", "Ref-002"])

for i in range(5):
    idmef.CorrelID.append(str(uuid.uuid4()))

idmef.AggrCondition.extend(["Source.IP", "Target.IP"])

for i in range(5):
    idmef.PredID.append(str(uuid.uuid4()))

for i in range(5):
    idmef.RelID.append(str(uuid.uuid4()))

# Analyzer
analyzer = idmef.Analyzer
analyzer.IP = "127.0.0.1"
analyzer.Name = "My Analyzer"
analyzer.Hostname = "localhost"
analyzer.Type = analyzer.AnalyzerTypeEnum.Type_Cyber
analyzer.Model = "MyAnalyzerV1"
analyzer.Category.append(analyzer.AnalyzerCategoryEnum.Category_HIDS)
analyzer.Data.append(analyzer.AnalyzerDataEnum.Data_Log)
analyzer.Method.append(analyzer.AnalyzerMethodEnum.Method_Statistical)
analyzer.GeoLocation = "48.1159863,-1.7234628"
analyzer.UnLocation = "FR RNS"
analyzer.Location = "France"

# Sensor
# Listed subclass must be added with the method .add()
sensor = idmef.Sensor.add()
sensor.IP = "127.0.0.1"
sensor.Name = "My Sensor"
sensor.Hostname = "localhost"
sensor.Model = "MySensorV1"
sensor.UnLocation = "FR RNS"
sensor.Location = "France"
sensor.CaptureZone = "My capture zone"

# Source
source = idmef.Source.add()
source.UnLocation = "FR RNS"
source.Location = "France"
source.GeoLocation = "48.1159863,-1.7234628"
source.Note = "A nice note about the source"
source.TI.extend(["Abuse.CH", "Spamhaus"])
source.IP = "127.0.0.1"
source.Hostname = "localhost"
source.User = "root"
source.Email = "root@comp.any"
source.Protocol.extend(["tcp", "ssh"])
source.Attachment.extend(["src_attach1", "src_attach2"])
source.Observable.extend(["src_obs1", "src_obs2"])

source = idmef.Source.add()
source.UnLocation = "FR RNS"
source.Location = "France"
source.GeoLocation = "48.1159863,-1.7234628"
source.Note = "A nice note about the second source"
source.IP = "10.0.0.35"
source.Hostname = "srv01"
source.User = "root"
source.Email = "root@comp.any"
source.Protocol.extend(["tcp", "ssh"])
source.Attachment.extend(["src2_attach1", "src2_attach2"])
source.Observable.extend(["src2_obs1", "src2_obs2"])

# Target
target = idmef.Target.add()
target.UnLocation = "FR RNS"
target.Location = "France"
target.GeoLocation = "48.1159863,-1.7234628"
target.Note = "A nice note about the target"
target.IP = "127.0.0.1"
target.Hostname = "localhost"
target.Service = "sshd"
target.User = "root"
target.Email = "root@comp.any"
target.Port.append(22)
target.Attachment.extend(["tgt_attach1", "tgt_attach2"])
target.Observable.extend(["tgt_obs1", "tgt_obs2"])

target = idmef.Target.add()
target.UnLocation = "FR RNS"
target.Location = "France"
target.GeoLocation = "48.1159863,-1.7234628"
target.Note = "A nice note about the second target"
target.IP = "10.0.0.5"
target.Hostname = "localhost"
target.Service = "sftp"
target.User = "root"
target.Email = "root@comp.any"
target.Port.extend([20, 21, 22])
target.Attachment.extend(["tgt2_attach1", "tgt2_attach2"])
target.Observable.extend(["tgt2_obs1", "tgt2_obs2"])

# Vector
vector = idmef.Vector.add()
vector.Category.extend([
    vector.VectorCategoryEnum.Vector_IPv4Address,
    vector.VectorCategoryEnum.Vector_EmailAddress,
    vector.VectorCategoryEnum.Vector_EmailMessage
])
vector.TI.append("Spamhaus")
vector.Name = "Unknown"
vector.Size = vector.VectorSizeEnum.Vector_Small
vector.UnLocation = "FR RNS"
vector.GeoLocation = "48.1159863,-1.7234628"
vector.GeoRadius = 0
vector.Location = "France"
vector.Note = "A nice note about the vector"
vector.Attachment.extend(["vct_attach1", "vct_attach2"])
vector.Observable.extend(["vct_obs1", "vct_obs2"])

# Attachment
for name in (
    "src_attach1", "src_attach2",
    "src2_attach1", "src2_attach2",
    "tgt_attach1", "tgt_attach2",
    "tgt2_attach1", "tgt2_attach2",
    "vct_attach1", "vct_attach2"):
    attach = idmef.Attachment.add()
    attach.Name = name
    attach.FileName = f"{name}.txt"
    attach.Hash = f"sha256:{hashlib.sha256(bytes(name, 'utf-8')).hexdigest()}"
    attach.Size = 4849
    attach.Ref.append('urn:clamav:Win.Trojan.Banker-14334')
    attach.ExternalURI.append('urn:mhr:55eaf7effadc07f866d1eaed9c64e7ee49fe081a')
    attach.Note = f"A nice note about {name}"
    attach.ContentType = "text"
    attach.ContentEncoding = "json"
    attach.Content = json.dumps({"test": 1, "test2": 2})

# Observable
for name in (
    "src_obs1", "src_obs2",
    "src2_obs1", "src2_obs2",
    "tgt_obs1", "tgt_obs2",
    "tgt2_obs1", "tgt2_obs2",
    "vct_obs1", "vct_obs2"):
    obs = idmef.Observable.add()
    obs.Name = name
    obs.Reference = "IDMEF-OBS"
    obs.Content = json.dumps({
        "type": "PTZ",
        "Pan": 34.00,
        "Tilt": -30.00,
        "Zoom": 18.00
    })

print(MessageToJson(idmef))
