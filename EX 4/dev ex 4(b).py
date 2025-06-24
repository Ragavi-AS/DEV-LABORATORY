import pandas as pd

data = {
    'employee': ['Alice','Bob','Charlie','Alice','Bob','Charlie'],
    'department': ['HR','HR','IT','IT','IT','HR'],
    'hours': [8, 7, 9, 6, 8, 7]
}
df = pd.DataFrame(data)


dept_group = df.groupby('department')['hours'].sum().reset_index(name='total_hours')
print("Total hours by department:\n", dept_group)


pivot_dept = df.pivot_table(index='department', values='hours',
                            aggfunc=['sum','mean','count'])
pivot_dept.columns = ['total_hours','avg_hours','count_entries']
print("\nPivot summary:\n", pivot_dept)

top_avg_dept = pivot_dept['avg_hours'].idxmax()
print(f"\nDepartment with highest average working hours: {top_avg_dept}")
