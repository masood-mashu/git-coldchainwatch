"""
eval_predictability.py - Checkpoint 02 Benchmark Suite for GitColdChainWatch.
"""
import os, sys, unittest
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from tools.temp_excursion_evaluator import *
from tools.mkt_kinetic_temp_calculator import *
from tools.transit_sla_auditor import *

class TestGitColdChainWatchPredictability(unittest.TestCase):

    def test_temp_excursion_evaluator(self):
        res = evaluate_temp_excursion('[4.5, 5.0, 5.2, 4.8, 5.1]')
        self.assertTrue(res["compliant"])
        self.assertEqual(res["status"], "COLD_CHAIN_MAINTAINED")

    def test_mkt_kinetic_temp_calculator(self):
        res = calculate_mkt('[4.0, 5.0, 6.0]')
        self.assertTrue(res["safe_range"])
        self.assertEqual(res["status"], "MKT_APPROVED")

    def test_transit_sla_auditor(self):
        res = audit_transit_sla(36.0, max_sla_hours=48.0)
        self.assertTrue(res["sla_met"])
        self.assertEqual(res["status"], "TRANSIT_SLA_MET")


if __name__ == "__main__":
    unittest.main()
