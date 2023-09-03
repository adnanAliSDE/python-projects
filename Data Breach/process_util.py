import psutil

# Iterate over all running process
chrome_processes = [proc for proc in psutil.process_iter() if proc.name().startswith('chrome')]
print(len(chrome_processes))

p1=chrome_processes[0]
print(p1.__doc__)
print(p1.children())