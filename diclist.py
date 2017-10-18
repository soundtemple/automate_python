letter_sent = False
format = 'pdf'
result_data = []
inner_dic = {
    'security': "sec",
    'name': "name",
    'status': "status",
    'invite': "yes" if letter_sent else ''
}

result_data.append(inner_dic)

if format == 'pdf':
    inner_dic['format'] = "pdf"

print(result_data)

payment_type = 'UTDs'

if payment_type in ["UTD", "AMT"]:
    print("YES")