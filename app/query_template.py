import pandas as pd
import matplotlib.pyplot as plt
import oracledb
import plotly.express as px


def get_db_connection():
    dsn = oracledb.makedsn('oracle.cise.ufl.edu', 1521, sid='orcl')  # should be the same
    un = 'ncomatas'  # oracle username (ufl)
    pw = ''  # oracle password (from CISE) FIXME: NEED COLES CISE PASSWORD
    conn = oracledb.connect(user=un, password=pw, dsn=dsn)
    return conn


# EACH QUERY HAS A FUNCTION CALL WITH INPUTS
def query_name(userInput1, userInput2):
    conn = get_db_connection()

    # SQL query
    query = f""" """ # INSERT QUERY HERE, USE {userInput1} FOR USER INPUT

    cursor = conn.cursor()
    cursor.execute(query)
    data = cursor.fetchall()
    cursor.close()
    conn.close()
    return data

data = query_name()

# FOR EACH COLUMN YOU WANT TO GRAPH/COLUMN FROM THE RESULT, NEED TO INSERT INTO A LIST
# THINK ABOUT WHAT WILL BE A LINE AND WHAT WILL BE ON THE AXES
x_axis_values = []
line1 = []
line2 = []

# NEED TO ITERATE THROUGH DATA, WHICH IS A LIST OF TUPLES, AND SPLIT IT INTO THE SEPARATE LISTS
# print(data) CAN BE USED TO SEE HOW THIS LIST IS FORMATTED
for tuple in data:
    x_axis_values.append(tuple[0])
    line1.append(tuple[1])
    line2.append(tuple[2])

# SELF EXPLANATORY I THINK
x_axis_column = 'year'  # idk if this actually matters
y_axis_columns = ['Stock Price Per Share of', 'Price of Gas'] # DETERMINES NAME ON LEGEND

# THIS IS WHERE DATA FOR THE PARTS OF THE GRAPH IS ACTUALLY CHOSEN!!!
x_axis = x_axis_values
y_axes = [line1, line2]

# PLOT ALL X AND Y AXES
for y_axis in y_axes:
    plt.plot(x_axis, y_axis)

# CREATE LABELS/NAMES FOR AXES AND TITLE
plt.xlabel('Year')
plt.ylabel('Value in $$$')
plt.title('Gas Price VS Stock Values')

# DISPLAY: PROBABLY SHOULD RETURN THIS TO THE FRONT END TO DISPLAY SOMEHOW
plt.legend(y_axis_columns)  # Add legend for clarity
plt.show()
