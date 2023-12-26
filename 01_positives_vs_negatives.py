def positives_and_negatives(*args):
    positives = 0
    negatives = 0
    for n in args:
        if n < 0:
            negatives += n
        else:
            positives += n

    print(negatives, positives, sep="\n")

    if positives > abs(negatives):
        return "The positives are stronger than the negatives"
    else:
        return "The negatives are stronger than the positives"


numbers = [int(x) for x in input().split()]

print(positives_and_negatives(*numbers))
