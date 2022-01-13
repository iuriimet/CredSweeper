
                'diff --git a/.changes/1.16.98.json b/.changes/1.16.98.json',
                'new file mode 100644',
                'index 00000000..7ebf3947',
                '--- /dev/null',
                '+++ b/.changes/1.16.98.json',
                '@@ -0,0 +1,4 @@',
                '+{',
                '+  "category": "``cloudformation``",',
                '+  "password": "dkajco1"',
                '+}',
                '',
                ''
    @mock.patch("logging.info")
    def test_load_patch_data_utf16_n(self, mock_logging_info: mock) -> None:
                'diff --git a/.changes/1.16.98.json b/.changes/1.16.98.json',
                'new file mode 100644',
                'index 00000000..7ebf3947',
                '--- /dev/null',
                '+++ b/.changes/1.16.98.json',
                '@@ -0,0 +1,4 @@',
                '+{',
                '+  "category": "``cloudformation``",',
                '+  "password": "dkajco1"',
                '+}',
                '',
                ''
        warning_message = f"UnicodeError: Can't read content from \"{file_path}\" as utf8."
        mock_logging_info.assert_called_once_with(warning_message)
    @mock.patch("logging.info")
    def test_load_patch_data_western_n(self, mock_logging_info: mock) -> None:
                'diff --git a/.changes/1.16.98.json b/.changes/1.16.98.json',
                'new file mode 100644',
                'index 00000000..7ebf3947',
                '--- /dev/null',
                '+++ b/.changes/1.16.98.json',
                '@@ -0,0 +1,4 @@',
                '+{',
                '+  "category": "``cloudformation``",',
                '+  "password": "dkajcö1"',
                '+}',
                '',
                ''
        warning_message = f"UnicodeError: Can't read content from \"{file_path}\" as utf16."
        mock_logging_info.assert_called_with(warning_message)
    @mock.patch("logging.info")
    def test_load_patch_data_n(self, mock_logging_info: mock) -> None:
                'ëÉÒÉÌÌÉÃÁ',
                'diff --git a/.changes/1.16.98.json b/.changes/1.16.98.json',
                'new file mode 100644',
                'index 00000000..7ebf3947',
                '--- /dev/null',
                '+++ b/.changes/1.16.98.json',
                '@@ -0,0 +1,4 @@',
                '+{',
                '+  "category": "``cloudformation``",',
                '+  "password": "dkajco1"',
                '+}',
                '',
                ''
        warning_message = f"UnicodeError: Can't read content from \"{file_path}\" as utf16."
        mock_logging_info.assert_called_with(warning_message)