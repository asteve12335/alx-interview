#!/usr/bin/python3

""" Module that returns a list of lists of integers representing
    the Pascal’s triangle of n """


def pascal_triangle(n):
  """
  Function that returns a list of lists of integers representing the Pascal's triangle of num_rows.

  Args:
    num_rows: The number of rows in the Pascal's triangle.

  Returns:
    A list of lists of integers representing the Pascal's triangle of num_rows.
  """

  if n <= 0:
    return []

  triangle = [[1]]

  for current_row in range(1, n):
    previous_row = triangle[-1]
    new_row = [1]

    for current_element in range(1, len(previous_row)):
      new_row.append(previous_row[current_element - 1] + previous_row[current_element])

    new_row.append(1)
    triangle.append(new_row)

  return triangle