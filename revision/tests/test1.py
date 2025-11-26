from revision import utils


def test_is_number_bigger_than_threshold_1():
    candidate_number = 10
    threshold = 20
    expected_result = False
    actual_result = utils.is_number_bigger_than_threshold(candidate_number=candidate_number, threshold=threshold)
    assert expected_result == actual_result


def test_is_number_bigger_than_threshold_2():
    candidate_number = 20
    threshold = 20
    expected_result = False
    actual_result = utils.is_number_bigger_than_threshold(candidate_number=candidate_number, threshold=threshold)
    assert expected_result == actual_result


def test_is_number_bigger_than_threshold_3():
    candidate_number = 0
    threshold = 0
    expected_result = False
    actual_result = utils.is_number_bigger_than_threshold(candidate_number=candidate_number, threshold=threshold)
    assert expected_result == actual_result