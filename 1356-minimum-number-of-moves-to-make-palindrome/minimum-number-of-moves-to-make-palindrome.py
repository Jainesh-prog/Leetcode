class Solution:
	def minMovesToMakePalindrome(self, s: str) -> int:
		s = list(s) #makes it easy for assignment op

		res = 0
		left, right = 0, len(s) - 1

		while left < right:
			l, r = left, right

			#find matching char
			while s[l] != s[r]:
				r -= 1

			# if index dont match then swap
			if l != r:
				# swap one by one
				while r < right:
					s[r], s[r + 1] = s[r + 1], s[r]
					res += 1
					r += 1

			else:
				s[r], s[r + 1] = s[r + 1], s[r]
				res += 1
				continue # get outside the main while loop

			left += 1
			right -= 1

		return res