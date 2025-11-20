import React from 'react';
import { render, screen } from '@testing-library/react';
import TaskList from './TaskList';

test('renders Task List heading', () => {
  render(<TaskList />);
  const headingElement = screen.getByText(/Task List/i);
  expect(headingElement).toBeInTheDocument();
});
