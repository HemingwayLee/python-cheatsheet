#!/usr/bin/env python3

import sqlite3

def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d

def print_table(rows):
    print("Content-Type: text/html\n")
    print("<!doctype html><h2>hello database</h2>")
    print("<table><tbody>")
    for row in rows:
        print("<td>")
        for col in row:
            print(f"<td>{row[col]}</td>")
        print("</tr>")
    print("</tbody></table>")


conn = sqlite3.connect("mydb", check_same_thread=False)
conn.row_factory = dict_factory
    
cur = conn.execute("SELECT * FROM mytbl;")
rows = cur.fetchall()
print_table(rows)

