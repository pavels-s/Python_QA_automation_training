import pytest

# Test case code must be written inside a method
# Medhod name must be strarted with "test"

a = 101

@pytest.mark.skipif(a>100, reason="Skipping as a>100")
def test_tc_001_Login_Logout_Testing():
    print("This is a first test case code")
    print("This is the end of test case")

@pytest.mark.smoke
def test_tc_003_Login_Logout_Invalid_credentials():
    print("This is my third testcase (smoke)")
    print("This is end of testcase")

# TIPS:
# Print display output on console   -s
# Verbose mode - display test cases name with status    -v
# Execute only specific testcase, what name is given    -k
# Execute only marked with specified tag     -m sanity (-s -m "smoke and sanity")