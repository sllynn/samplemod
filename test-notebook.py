# Databricks notebook source
import sample
sample.hmm()

# COMMAND ----------

from unittest import TestResult, TestLoader
from tests.test_advanced import AdvancedTestSuite

# COMMAND ----------

TestLoader().loadTestsFromTestCase(AdvancedTestSuite).run(TestResult())
