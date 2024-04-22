class employee:
    def __init__(self, name, cpf, rg):
        self.name = name
        self.cpf = cpf
        self.rg = rg


class employee_hourly(employee):
    def __init__(self, name, cpf, rg, work_hours, payment_hours):
        employee.__init__(self, name, cpf, rg)
        self.work_hours = work_hours
        self.payment_hours = payment_hours

    def payment(self):
        # Quantidade pagamento multiplicado pelas horas trabalhadas.
        return self.payment_hours * self.work_hours


class employee_CLT(employee):
    def __init__(self, name, cpf, rg, wage):
        employee.__init__(self, name, cpf, rg)
        self.wage = wage

    def payment(self):
        return 13.3 * self.wage


class service_provider(employee):
    def __init__(self, name, cpf, rg, loose):
        employee.__init__(self, name, cpf, rg)
        self.loose = loose

    def payment(self):
        return self.loose


# Employee Test
emp = employee('User', '000.000.000-XX', '00-000-000-X')
print(f'\033[1mName\033[m: {emp.name}\n\033[1mCPF\033[m: {emp.cpf}\n\033[1mRG\033[m: {emp.rg}\n')


# Hours pay
print('\033[1mPayment Hours\033[m')
emphour = employee_hourly(emp.name, emp.cpf, emp.rg, 30, 10)
print(f'{emphour.work_hours} hours and R${emphour.payment_hours} gets \033[32mR${emphour.payment():.2f}\033[m in the work.\n')


# CLT Test
print('\033[1mPayment Month\033[m')
empclt = employee_CLT(emp.name, emp.cpf, emp.rg, 31 * 6)    # 6 hours each day of the month
print(f'{emp.name} get in the month \033[32mR${empclt.payment():.2f}\033[m\n')


# Provider Test
print('\033[1mProvider Test\033[m')
pvd = service_provider(emp.name, emp.cpf, empclt.rg, 500)
print(f'Service provider gets \033[32mR${pvd.payment():.2f}\033[m')
