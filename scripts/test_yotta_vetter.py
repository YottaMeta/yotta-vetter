# -*- coding: utf-8 -*-
"""yotta-vetter（元审）测试套件。

用法：
  python3 scripts/test_yotta_vetter.py
覆盖：check 干净/恶意/自扫、四阶段清单、JSON 与报告、严重级过滤、
V3 元安联动、source 来源检查（格式/404 降级）、GBK 控制台加固。
"""
import json
import os
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

HERE = Path(__file__).resolve().parent
SCRIPT = HERE / "yotta_vetter.py"
FIX = HERE.parent.parent.parent / ".tmp" / "audit-fixtures"


def run_cli(args, env=None):
    full = dict(os.environ)
    if env:
        full.update(env)
    return subprocess.run(
        [sys.executable, str(SCRIPT)] + args,
        capture_output=True, text=True, encoding="utf-8", errors="replace",
        env=full, timeout=60,
    )


class VetterCliTest(unittest.TestCase):
    def test_check_clean(self):
        r = run_cli(["check", str(FIX / "clean-skill"), "--no-color"])
        self.assertEqual(r.returncode, 0, r.stdout + r.stderr)
        self.assertIn("SAFE TO INSTALL", r.stdout)

    def test_check_evil_verdict_and_linkage(self):
        r = run_cli(["check", str(FIX / "evil-skill"), "--no-color"])
        self.assertEqual(r.returncode, 3, r.stdout + r.stderr)
        self.assertIn("DO NOT INSTALL", r.stdout)
        self.assertIn("yotta-security-audit --target skill", r.stderr)  # V3 联动

    def test_check_self_no_high_critical(self):
        """自扫：无 high/critical（urllib 来源检查为预期 medium，规则表已豁免）。"""
        r = run_cli(["check", str(SCRIPT.parent), "--no-color"])
        self.assertIn(r.returncode, (0, 1), r.stdout + r.stderr)
        self.assertNotIn("[HIGH]", r.stdout)
        self.assertNotIn("[CRITICAL]", r.stdout)

    def test_check_missing_path_exit4(self):
        r = run_cli(["check", "C:/definitely/not/exists"])
        self.assertEqual(r.returncode, 4, r.stdout + r.stderr)

    def test_check_json(self):
        r = run_cli(["check", str(FIX / "evil-skill"), "--json"])
        self.assertEqual(r.returncode, 3, r.stderr)
        data = json.loads(r.stdout)
        self.assertEqual(data["tool"], "yotta-vetter")
        self.assertGreaterEqual(data["summary"]["critical"], 1)
        self.assertTrue(all("rule_id" in f for f in data["findings"]))

    def test_check_report_md(self):
        with tempfile.TemporaryDirectory() as td:
            rep = Path(td) / "vetting-report.md"
            r = run_cli(["check", str(FIX / "evil-skill"), "--report", str(rep)])
            self.assertEqual(r.returncode, 3, r.stderr)
            self.assertTrue(rep.exists())
            txt = rep.read_text(encoding="utf-8")
            self.assertIn("SKILL VETTING REPORT", txt)
            self.assertIn("决策记录", txt)

    def test_check_severity_filter(self):
        r = run_cli(["check", str(FIX / "evil-skill"),
                     "--severity", "critical", "--no-color"])
        self.assertEqual(r.returncode, 3, r.stderr)
        self.assertNotIn("[MEDIUM]", r.stdout)

    def test_inventory_missing_skill_md(self):
        with tempfile.TemporaryDirectory() as td:
            Path(td, "README.md").write_text("no skill", encoding="utf-8")
            r = run_cli(["check", td, "--no-color"])
            self.assertIn("缺少 SKILL.md", r.stdout)

    def test_source_bad_format_exit4(self):
        r = run_cli(["source", "not-a-slash-spec"])
        self.assertEqual(r.returncode, 4, r.stdout + r.stderr)

    def test_source_missing_repo_exit1(self):
        r = run_cli(["source", "github:YottaMeta/__no_such_repo_xyz__"])
        self.assertEqual(r.returncode, 1, r.stdout + r.stderr)

    def test_bad_command_exit4(self):
        r = run_cli(["frobnicate"])
        self.assertEqual(r.returncode, 4, r.stdout + r.stderr)

    def test_gbk_console_no_crash(self):
        env = dict(os.environ)
        env["PYTHONIOENCODING"] = "gbk"
        r = subprocess.run(
            [sys.executable, str(SCRIPT), "check", str(FIX / "clean-skill"), "--no-color"],
            capture_output=True, env=env, timeout=60)
        self.assertEqual(r.returncode, 0, r.stderr.decode("gbk", errors="replace"))
        self.assertNotIn(b"UnicodeEncodeError", r.stderr)


if __name__ == "__main__":
    suite = unittest.defaultTestLoader.loadTestsFromModule(sys.modules[__name__])
    ok = unittest.TextTestRunner(verbosity=2).run(suite).wasSuccessful()
    sys.exit(0 if ok else 1)
