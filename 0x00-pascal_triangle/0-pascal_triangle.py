#!/usr/bin/python3
"""This is a  pascal triangle function"""



def pascal_triangle(n):
  """
  This function generates Pascal's triangle up to n rows.

  Args:
      n: The number of rows in the Pascal's triangle.

  Returns:
      A list of lists representing the Pascal's triangle.
  """

  if n <= 0:
    return []

  triangle = []
  # First row is always [1]
  triangle.append([1])

  # Iterate for remaining rows
  for i in range(1, n):
    previous_row = triangle[i - 1]
    current_row = []
    # First and last element of each row are always 1
    current_row.append(1)

    # Calculate elements in the middle based on previous row
    for j in range(1, i):
      current_row.append(previous_row[j - 1] + previous_row[j])

    current_row.append(1)
    triangle.append(current_row)

  return triangle

