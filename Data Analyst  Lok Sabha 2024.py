#!/usr/bin/env python
# coding: utf-8

# In[ ]:


pip install mysql-connector-python


# In[4]:


import matplotlib.pyplot as plt
import seaborn as sns

# 1. Political Landscape
labels = ['BJP-led NDA', 'INDIA Coalition', 'Congress', 'Others']
sizes = [240, 234, 99, 30]  # Number of seats won by each group

plt.figure(figsize=(8, 6))
plt.bar(labels, sizes, color=['blue', 'green', 'orange', 'gray'])
plt.title('Political Landscape of the 2024 Lok Sabha Election')
plt.xlabel('Political Parties/Coalitions')
plt.ylabel('Number of Seats Won')
plt.xticks(rotation=45)
plt.show()

# 2. Voter Turnout and Gender Participation
total_voters = 968e6
voters_participated = 642e6
voters_female = 312e6
voters_male = voters_participated - voters_female

sizes = [voters_participated, voters_female, voters_male]
labels = ['Total Voters', 'Female Voters', 'Male Voters']
colors = ['skyblue', 'orange', 'lightgreen']

plt.figure(figsize=(8, 6))
plt.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', startangle=140)
plt.title('Voter Turnout and Gender Participation')
plt.axis('equal')
plt.show()

# 3. Campaign Narrative Comparison
party_labels = ['BJP', 'Congress']
economic_focus = [70, 40]  # Hypothetical percentages of campaign focus on economic reforms
social_focus = [30, 60]   # Hypothetical percentages of campaign focus on social welfare
x = range(len(party_labels))

plt.figure(figsize=(8, 6))
plt.bar(x, economic_focus, width=0.4, label='Economic Focus', color='blue')
plt.bar(x, social_focus, width=0.4, label='Social Focus', color='orange', bottom=economic_focus)
plt.xticks(x, party_labels)
plt.title('Campaign Narrative Comparison')
plt.xlabel('Political Parties')
plt.ylabel('Percentage of Focus')
plt.legend()
plt.show()


# In[ ]:





# In[ ]:




