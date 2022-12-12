"""
TESTS is a dict with all of your tests.
Keys for this will be the categories' names.
Each test is a dict with
    "input" -- input data for a user function
    "answer" -- your right answer
    "explanation" -- not necessarily a key, it's used for an additional info in animation.
"""


TESTS = {
    "Basics": [
        {
            "input": [4],
            "answer": '4',
            "explanation": "4th Ugly number is..."
        },
        {
            "input": [6],
            "answer": '6',
            "explanation": "6th Ugly number is..."
        },
        {
            "input": [11],
            "answer": '15',
            "explanation": "11th Ugly number is..."
        },
        {
            "input": [1],
            "answer": '1',
            "explanation": "1st Ugly number is..."
        },
        {
            "input": [29],
            "answer": '75',
            "explanation": "Result is below 100..."
        },
        {
            "input": [84],
            "answer": '960',
            "explanation": "Result is below 1000..."
        },
        {
            "input": [171],
            "answer": '9216',
            "explanation": "Over nine thousands!"
        },
        {
            "input": [313],
            "answer": '100000',
            "explanation": "Jackpot!"
        },
        {
            "input": [593],
            "answer": '2332800',
            "explanation": "It's getting harder..."
        },
        {
            "input": [899],
            "answer": '26214400',
            "explanation": "Too slow?.. It's not the end..."
        },
        {
            "input": [978],
            "answer": '44789760',
            "explanation": "Where are you turn the wrong way?"
        },
        {
            "input": [1173],
            "answer": '150000000',
            "explanation": "150 billions!"
        },
        {
            "input": [1398],
            "answer": '512000000',
            "explanation": "150 billions!"
        },
        {
            "input": [1407],
            "answer": '536870912',
            "explanation": "2 ** 29"
        },
        {
            "input": [1500],
            "answer": '859963392',
            "explanation": "Previous task final test!"
        },
        {
            "input": [9999],
            "answer": '288230376151711744',
            "explanation": "4 digits --> 18 digits"
        }
    ],
    "Extra": [
        {
            "input": [103569],
            "answer": '838860800000000000000000000000000000000',
            "explanation": "Over 100k"
        },
        {
            "input": [345687],
            "answer": '34171875000000000000000000000000000000000000000000000000000',
            "explanation": "Over 300k"
        },
        {
            "input": [567890],
            "answer": '1581200997733716346496120527672154746617978577134207218620890611712000',
            "explanation": "Over 500k"
        },
        {
            "input": [777777],
            "answer": '84918008465300059964874363721276554891160246371507857522688000000000000000000',
            "explanation": "Double 3-Axes"
        },
        {
            "input": [1000000],
            "answer": '519312780448388736089589843750000000000000000000000000000000000000000000000000000000',
            "explanation": "The final test!"
        }
    ]
}
