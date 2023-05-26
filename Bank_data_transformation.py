# Databricks notebook source
df = spark.read.option('header',True).csv('dbfs:/FileStore/tables/bank__1_.csv')
display(df)
