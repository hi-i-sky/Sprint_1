types = {
    1: 'Блокирующий',
    2: 'Критический',
    3: 'Значительный',
    4: 'Незначительный',
    5: 'Тривиальный'
} 

tickets = {
    1: ['API_45', 'API_76', 'E2E_4'],
    2: ['UI_19', 'API_65', 'API_76', 'E2E_45'],
    3: ['E2E_45', 'API_45', 'E2E_2'],
    4: ['E2E_9', 'API_76'],
    5: ['E2E_2', 'API_61']
} 

def fix_tikets(tickets):
    fixed_tickets_dict = {}
    unic_tickets = []
    for key, value in tickets.items():
        list_unic_tickets = []
        for ticket in value:
            if ticket not in unic_tickets:
                unic_tickets.append(ticket)
                list_unic_tickets.append(ticket)
        fixed_tickets_dict[key] = list_unic_tickets
    return fixed_tickets_dict

def result_dict(types, tickets):
    tickets_by_type = {}
    for i in range(1, 6):
        tickets_by_type[types.get(i)] = tickets.get(i)
    return tickets_by_type


        

            