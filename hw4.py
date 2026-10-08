web_development = ['Rahul', 'Anu', 'Arjun']

data_science = ['Akhil', 'Meera', 'Vishnu']

ui_ux_design = ['Neha', 'Riya', 'Adithya']
all_participants =[web_development,data_science,ui_ux_design]
print(all_participants)
web_development.append("sajith")
print(web_development)
data_science.insert(1,"nikhil")
print(data_science)
ui_ux_design.pop()
print(ui_ux_design)
datas=data_science.copy()
print(datas)
data_science.clear()
print(data_science)
print(web_development[:2])
print(web_development)
lengthh=[len(x) for x in datas]
print(lengthh)
web_development = ['Rahul', 'Anu', 'Arjun']
data_science = ['Akhil', 'Meera', 'Vishnu']
ui_ux_design = ['Neha', 'Riya', 'Adithya']

# Check whether Asha is in any workshop list
if 'Asha' in web_development or 'Asha' in data_science or 'Asha' in ui_ux_design:
    print("Asha is a participant")
else:
    print("Asha is not a participant")

# Tuple containing the first participant from each workshop
first_participants = (
    web_development[0],
    data_science[0],
    ui_ux_design[0]
)

print(first_participants)