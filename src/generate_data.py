from faker import Faker
import pandas as pd
import random

fake = Faker('es_ES')
random.seed(42)

def generate_departments(): #Genera despartamentos
    names = ["Finanzas","IT","RRHH","Legal","Marketing","Produccion","Directiva"]
    depts = []
    for i, name in enumerate(names, start=1):
        depts.append({
            "dept_id": i,
            "dept_name": name,
        })
    return pd.DataFrame(depts)


def generate_jobs(n=25): # Genera puestos de trabajo. 
    names = [ #Matriz con los nombres de los puestos por departamento 
    ["Contador Junior", "Contador Senior", "Analista Financiero", "Manager de Finanzas"],
    ["Ingeniero Junior", "Ingeniero Mid", "Ingeniero Senior","Product Manager"],
    ["Especialista en Reclutamiento", "Coordinador de RRHH", "Especialista de nomina", "Manager de RRHH"],
    ["Abogado Junior", "Abogado Senior", "Asesor Legal","Abogado Jefe"],
    ["Especialista en Marketing Digital", "Coordinador de Marketing", "Analista de Marketing", "Manager de Marketing"],
    ["Operario", "Supervisor de Producción", "Ingeniero de Procesos", "Manager de Producción"],
    ["Secretario auxiliar", "Secretario", "Asistente Ejecutivo", "Gerente General"]]
    jobs = []
    for i in range(1, n+1): 
        dept = random.randint(1, 7) #Selecciona un departamento aleatorio primero
        jobs.append({
            "job_id": i,
            "job_name": random.choice(names[dept-1]), #Selecciona un nombre de puesto aleatorio del departamento seleccionado
            "job_salary": random.randint(1000, 20000), #Salario aleatorio
            "job_dept": dept #Guarda el departamento 
        })
    return pd.DataFrame(jobs)


def generate_employees(n=100, departments_df=None, jobs_df=None): #Genera empleados. Depende de Departamentos y Puestos
    employees = []
    for i in range(1, n+1):
        dept_id = 0
        if departments_df is not None:
            dept_id = int(departments_df.sample(1)["dept_id"].iloc[0]) #Escoge departamento aleatorio
        if jobs_df is not None:
            job_id = int(jobs_df[jobs_df["job_dept"] == dept_id].sample(1)['job_id']) #Escoge un puesto aleatorio del departamento seleccionado
        employees.append({
            "emp_id": i,
            "first_name": fake.first_name(),
            "last_name": fake.last_name(),
            "email": fake.email(),
            "phone_number": fake.phone_number(),
            "dept_id": dept_id,
            "job_id":job_id
        })
    return pd.DataFrame(employees)

# Uso
depts = generate_departments()
jobs = generate_jobs(30)
employees = generate_employees(500, depts, jobs)
#print(depts)
#print(positions)
#print(employees)

#Save to CSV
depts.to_csv("src/raw/departments.csv",sep=",", index=False)
jobs.to_csv("src/raw/jobs.csv", index=False)
employees.to_csv("src/raw/employees.csv", index=False)



