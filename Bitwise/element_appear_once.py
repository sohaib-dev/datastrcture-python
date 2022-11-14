def getSingle(arr, n):
    ones = 0
    twos = 0

    for i in range(n):
        # one & arr[i]" gives the bits that
        # are there in both 'ones' and new
        # element from arr[]. We add these
        # bits to 'twos' using bitwise XOR
        print(bin(arr[i]))
        print(bin(ones))
        print(bin(twos))
        twos = twos ^ (ones & arr[i])
        print(bin(twos))

        # one & arr[i]" gives the bits that
        # are there in both 'ones' and new
        # element from arr[]. We add these
        # bits to 'twos' using bitwise XOR
        ones = ones ^ arr[i]
        print(bin(ones))

        # The common bits are those bits
        # which appear third time. So these
        # bits should not be there in both
        # 'ones' and 'twos'. common_bit_mask
        # contains all these bits as 0, so
        # that the bits can be removed from
        # 'ones' and 'twos'
        common_bit_mask = ~(ones & twos)
        print(bin(ones & twos))
        print(bin(common_bit_mask))

        # Remove common bits (the bits that
        # appear third time) from 'ones'
        ones &= common_bit_mask
        print(bin(ones))

        # Remove common bits (the bits that
        # appear third time) from 'twos'
        twos &= common_bit_mask
        print(bin(twos))

    return ones


# driver code
arr = [3, 3, 2, 3]
n = len(arr)
print("The element with single occurrence is ",
      getSingle(arr, n))
