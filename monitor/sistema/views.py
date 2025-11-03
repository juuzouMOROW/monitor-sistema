import psutil
import platform
from django.shortcuts import render
from datetime import datetime

def get_system_info():
    """Función para obtener información del sistema con manejo de errores"""
    try:
        #Aca la información del CPU
        cpu_percent = psutil.cpu_percent(interval=1)
        cpu_cores = psutil.cpu_count(logical=False) or "N/A"
        cpu_threads = psutil.cpu_count(logical=True) or "N/A"
        
        #Aca la información de memoria RAM
        memory = psutil.virtual_memory()
        memory_total_gb = round(memory.total / (1024**3), 2)
        memory_used_gb = round(memory.used / (1024**3), 2)
        memory_percent = memory.percent
        
        #Aca la información del disco
        disk = psutil.disk_usage('/')
        disk_total_gb = round(disk.total / (1024**3), 2)
        disk_used_gb = round(disk.used / (1024**3), 2)
        disk_free_gb = round(disk.free / (1024**3), 2)
        disk_percent = disk.percent
        
        # Aca la información del sistema operativo
        system_os = f"{platform.system()} {platform.release()}"
        system_arch = platform.architecture()[0]
        system_processor = platform.processor() or "N/A"
        
        return {
            'cpu_percent': cpu_percent,
            'cpu_cores': cpu_cores,
            'cpu_threads': cpu_threads,
            'memory_total_gb': memory_total_gb,
            'memory_used_gb': memory_used_gb,
            'memory_percent': memory_percent,
            'disk_total_gb': disk_total_gb,
            'disk_used_gb': disk_used_gb,
            'disk_free_gb': disk_free_gb,
            'disk_percent': disk_percent,
            'system_os': system_os,
            'system_arch': system_arch,
            'system_processor': system_processor,
            'current_time': datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        }
        
    except Exception as e:
        # Manejo de errores
        return {
            'error': f"No se pudieron obtener los datos del sistema: {str(e)}",
            'cpu_percent': 0,
            'cpu_cores': "Error",
            'cpu_threads': "Error",
            'memory_total_gb': 0,
            'memory_used_gb': 0,
            'memory_percent': 0,
            'disk_total_gb': 0,
            'disk_used_gb': 0,
            'disk_free_gb': 0,
            'disk_percent': 0,
            'system_os': "Error",
            'system_arch': "Error",
            'system_processor': "Error",
            'current_time': datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        }

def index(request):
    """Vista principal que muestra la página con los datos del sistema"""
    system_data = get_system_info()
    return render(request, 'sistema/index.html', system_data)