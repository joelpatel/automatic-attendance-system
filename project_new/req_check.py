import requests
import json
data={
    "name":"kirtan",
    "enroll":"7063"
}
#
# res=requests.post(url="http://localhost:3000/users/add_attendance",data=data)
#
# resdata=res.text
# print(resdata)
data={

}
res=requests.get(url="http://localhost:3000/users/get_student_data")
resdata=json.loads(res.text)

for i in range(len(resdata)):
    data[resdata[i]['rollno']]=resdata[i]['name']




print(data)
