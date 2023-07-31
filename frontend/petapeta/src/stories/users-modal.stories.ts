import type { Meta, StoryObj } from '@storybook/react';
import { UserListItem } from '../app/organisms/users-modal';

const meta = {
    title: 'User List Item',
    component: UserListItem,
    tags: ['autodocs'],
    parameters: {
        layout: 'fullscreen',
    },
} satisfies Meta<typeof UserListItem>;

export default meta;

type Story = StoryObj<typeof meta>;

export const Default: Story = {
    args: {
        name: 'Jane Doe',
        numLikes: 0,
    },
};