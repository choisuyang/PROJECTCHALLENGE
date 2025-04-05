# custom_allure_formatter.py
from allure_behave.formatter import AllureFormatter as BaseAllureFormatter
import time
import os

class AllureFormatter(BaseAllureFormatter):
    def _write_test_result(self, test_result):
        # ⏰ 타임스탬프 + UUID를 파일명으로 사용
        timestamp = time.strftime("%Y-%m-%d_%H-%M-%S")
        filename = f"{timestamp}_{test_result.uuid}-result.json"

        # 저장 경로 구성
        output_dir = self.config.formatter_opts.get("output", "allure-results")
        path = os.path.join(output_dir, filename)

        # 결과 저장
        with open(path, "w", encoding="utf-8") as f:
            self.serializer(test_result, f)