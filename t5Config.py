import torch
import os


class Config(object):
    sentence_total = 30
    word_sentence = 20
    batch_size = 2
    label_words = {
        "No": ["NonVulIssueReport", "NormalBug"],
        "Yes": ["VulIssueReport", "IssueWithVulnerability"]
    }
    classes = [
        'No', 'Yes'
    ]
    selection_map = {
        'C1': 'the first code.', 'C2': 'the second code.',
        'C3': 'the third code.',
        'C4': 'the fourth code.', 'C5': 'no such code.'}
    steps = 500
    save_steps = 10
    aug_times = 10
    PROB = 0.3
    train_test_prop = 0.8
    generation_arguments = {
        "max_length": 10,
        "max_new_tokens": None,
        "temperature": 1.0,
        "do_sample": False,
        "top_k": 0,
        "top_p": 0.9,
        "repetition_penalty": 1.0,
        "num_beams": 5,
    }
