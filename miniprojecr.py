import json 
class task :
    def __init__(self,title,desc,deadline,done =False):
        self.title=title
        self.desc=desc
        self.dealine=deadline
        self.done=done 
class todoapp:
    def __init__(self,filename="tasks.json"):
        self.filename=filename
        self.tasks=[]
    def load_tasks(self):
        try:
            with open(self.filename,"r",encoding="utf-8") as f :
                return json.load (f)
        except:
            return []
    def save_tasks (self):
        with open (self.filename,"w",encoding="utf-8") as f :
            json.dump(self.tasks,f,ensure_ascii=False,indent=2) 
    def add_task(self,title,desc,deadline):
        self.tasks.append({
            "title":title,
            "desc":desc,
            "deadline":deadline,
            "done":False 
        })
        self.save_tasks()
    def list_tasks(self):
        for i,t in enumerate(self.tasks,1):
            status="✓" if t["done"] else "✗"
            print(f"{i}. [{status}] {t['title']} - {t['desc']} (Due: {t['deadline']})")    

app=todoapp()
app.add_task("Hoc python","on oop va lam mini project","2025-09-02")
app.list_tasks()                           


        

