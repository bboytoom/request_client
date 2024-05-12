class AssertGeneral:

    def assert_json_result(self,
                           result,
                           expected_exceptions: dict | None):

        self.assertIsInstance(result, dict)
        self.assertEqual(result, expected_exceptions)
