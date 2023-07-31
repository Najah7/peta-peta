import type { Meta, StoryObj } from '@storybook/react';
import { NamedAvatar } from '../app/molecules/named-avatar';

const meta = {
    title: 'Named Avatar',
    component: NamedAvatar,
    // This component will have an automatically generated Autodocs entry: https://storybook.js.org/docs/react/writing-docs/autodocs
    tags: ['autodocs'],
    parameters: {
        // More on how to position stories at: https://storybook.js.org/docs/react/configure/story-layout
        layout: 'fullscreen',
    },
} satisfies Meta<typeof NamedAvatar>;

export default meta;
type Story = StoryObj<typeof meta>;

export const Default: Story = {
    args: {
        name: 'Jane Doe',
    },
};

export const WithImage: Story = {
    args: {
        name: 'Jane Doe',
        avatarUrl: 'https://mui.com/static/images/avatar/1.jpg',
    },
};

export const WithImageAndSize: Story = {
    args: {
        name: 'Jane Doe',
        avatarUrl: 'https://mui.com/static/images/avatar/1.jpg',
        size: 100,
    },
};

export const WithImageAndColor: Story = {
    args: {
        name: 'Jane Doe',
        avatarUrl: 'https://mui.com/static/images/avatar/1.jpg',
        color: 'red',
    },
};
        

