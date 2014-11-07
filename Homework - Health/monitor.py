import psutil, datetime
from wsgiref.simple_server import make_server

def getOutput():
        output = '' ;
        THRESHOLD = 100 * 1024 * 1024  # 100MB
        boot_time = datetime.datetime.fromtimestamp(psutil.boot_time()).strftime("%Y-%m-%d %H:%M:%S")
        cpu_util = psutil.cpu_percent(interval=1, percpu=True)
        mem = psutil.virtual_memory()

        output ='<table width="40%" border="0"><tbody><tr bgcolor="#CEF6F5"><td>BOOT TIME</td><td>'+boot_time+'</td></tr><tr><td>CPU UTILIZATION</td><td><table border="0" width="100%"><tbody>'
        i=1
        for cpu in cpu_util:
            output = output + '<tr><td>CPU ' + str(i) + '</td><td bgcolor="#E2A9F3">' + str(cpu) + '</td></tr>';
            i+=1 ;
        output = output + '</tbody></table></td></tr><tr bgcolor="#CEF6F5"><td>AVAILABLE MEMORY</td><td>'+str(mem.available)+ '</td></tr><tr><td>USED MEMORY</td><td>'+str(mem.used)+'</td></tr><tr bgcolor="#CEF6F5"><td>USED PERCENTAGE</td><td>'+str(mem.percent)+'</td></tr></tbody></table>'
        return output;

def montior(environ, start_response):
	status = '200 OK'
	headers = [('Content-type', 'html; charset=utf-8')]
	start_response(status, headers)
	message = getOutput();
	return[bytes(message,'utf-8')]

httpd = make_server('', 8000, montior)
print("Serving on port 8000...")
httpd.serve_forever()