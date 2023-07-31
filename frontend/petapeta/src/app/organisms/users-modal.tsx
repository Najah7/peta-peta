import * as React from 'react';
import Divider from '@mui/material/Divider';
import Typography from '@mui/material/Typography';
import Box from '@mui/material/Box';
import ClearIcon from '@mui/icons-material/Clear';
import IconButton from '@mui/material/IconButton';
import { UserList } from '../molecules/user-list';

interface Props {
    name: string;
    numLikes: number;
    oneLineIntroduction?: string;
    avatarUrl?: string;
}

export const UserListItem: React.FC<Props> = ({
    name,
    numLikes,
    oneLineIntroduction='This is a one line introduction.',
    avatarUrl='/sample/user/anonymous.jpg',
}): JSX.Element => {
  return (
    <Box sx={{border: "3px solid #ea7b25", borderRadius: "40px", padding: "0", margin: "10px", width: "35vw"}}>
        <Box sx={{ display: 'flex', padding: "0 30px", justifyContent: "space-between" }}>
            <Typography variant="h6">
                Likes💙： {numLikes}
            </Typography>
            <IconButton aria-label="clear" >
                <ClearIcon />
            </IconButton>
        </Box>
        <Divider variant="fullWidth" sx={{backgroundColor: "#ea7b25", borderWidth: "1px"}} />
        <Box>
            <UserList name={name} oneLineIntroduction={oneLineIntroduction} avatarUrl={avatarUrl} />
        </Box>
    </Box>
  );
}