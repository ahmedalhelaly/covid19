# # -*- coding: utf-8 -*-
#
# # Define your item pipelines here
# #
# # Don't forget to add your pipeline to the ITEM_PIPELINES setting
# # See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
#
# import sqlite3
#
# class covid19Pipeline(object):
#
#     table_name = "COVUPDATES"
#
#     def __init__(self):
#         self.create_connection()
#         self.create_table()
#
#     def create_connection(self):
#         self.conn = sqlite3.connect("COV.db")
#         self.curr = self.conn.cursor()
#
#     def create_table(self):
#         self.curr.execute(f""" DROP TABLE IF EXISTS {self.table_name}""")
#         self.curr.execute(f""" CREATE TABLE {self.table_name}(
#                                 COUNTRY         TEXT PRIMARY_KEY,
#                                 TOTAL_CASES     TEXT,
#                                 NEW_CASES       TEXT,
#                                 TOTAL_DEATHS    TEXT,
#                                 NEW_DEATHS      TEXT,
#                                 TOTAL_RECOVERED TEXT,
#                                 ACTIVE_CASES    TEXT,
#                                 CRITICAL_CASES  TEXT) """)
#
#     def process_item(self, item, spider):
#         self.store_data(item)
#         return item
#
#     def store_data(self, item):
#         self.curr.execute(f""" INSERT INTO {self.table_name} VALUES(
#                                 ?, ?, ?, ?, ?, ?, ?, ?) """,
#                                 (item['country'],
#                                 item['total_cases'],
#                                 item['new_cases'],
#                                 item['total_deaths'],
#                                 item['new_deaths'],
#                                 item['total_recovered'],
#                                 item['active_cases'],
#                                 item['critical_cases']))
#         self.conn.commit()