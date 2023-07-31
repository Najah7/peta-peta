import type { Meta, StoryObj } from '@storybook/react';
import { NamedIconButton } from '../app/molecules/named-icon-button';

const meta = {
    title: 'Named Icon Button',
    component: NamedIconButton,
    tags: ['autodocs'],
    parameters: {
        layout: 'fullscreen',
    },
} satisfies Meta<typeof NamedIconButton>;

export default meta;

type Story = StoryObj<typeof meta>;

export const Default: Story = {
    args: {
        text: 'Button',
    },
};

export const WithImage: Story = {
    args: {
        text: 'Button',
        iconUrl: 'https://mui.com/static/images/avatar/1.jpg',
    },
};

export const WithImageAndSize: Story = {
    args: {
        text: 'Button',
        iconUrl: 'https://mui.com/static/images/avatar/1.jpg',
        size: 100,
    },
};

export const WithImageAndConsoleLog: Story = {
    args: {
        text: 'Button',
        iconUrl: 'https://mui.com/static/images/avatar/1.jpg',
        onClick: () => console.log('Clicked!'),
    },
};