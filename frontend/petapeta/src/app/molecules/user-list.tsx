import React from "react";
import List from '@mui/material/List';
import ListItem from '@mui/material/ListItem';
import Divider from '@mui/material/Divider';
import ListItemText from '@mui/material/ListItemText';
import ListItemAvatar from '@mui/material/ListItemAvatar';
import Avatar from '@mui/material/Avatar';
import Typography from '@mui/material/Typography';

interface Props {
    name: string;
    oneLineIntroduction?: string;
    avatarUrl?: string;
}


export const UserList: React.FC<Props> = ({
    name,
    oneLineIntroduction='This is a one line introduction.',
    avatarUrl='/sample/user/anonymous.jpg',
}): JSX.Element => {
    return (
        // TODO: mapを使って、ユーザーのリストを表示するように修正する。オブジェクトについてまだ未定なので、一旦放置。
        <List sx={{ width: '100%', maxWidth: 360 }}>
                <ListItem alignItems="flex-start">
                    <ListItemAvatar>
                    <Avatar alt="Remy Sharp" src={avatarUrl} />
                    </ListItemAvatar>
                    <ListItemText
                    primary={name}
                    secondary={
                        <React.Fragment>
                        <Typography
                            sx={{ display: 'inline' }}
                            component="span"
                            variant="body2"
                            color="text.primary"
                        >
                            Ali Connors
                        </Typography>
                        {oneLineIntroduction}
                        </React.Fragment>
                    }
                    />
                </ListItem>
                <Divider variant="inset" component="li" />
                <ListItem alignItems="flex-start">
                    <ListItemAvatar>
                    <Avatar alt="Travis Howard" src={avatarUrl} />
                    </ListItemAvatar>
                    <ListItemText
                    primary={name}
                    secondary={
                        <React.Fragment>
                        <Typography
                            sx={{ display: 'inline' }}
                            component="span"
                            variant="body2"
                            color="text.primary"
                        >
                            to Scott, Alex, Jennifer
                        </Typography>
                        {oneLineIntroduction}
                        </React.Fragment>
                    }
                    />
                </ListItem>
                <Divider variant="inset" component="li" />
                <ListItem alignItems="flex-start">
                    <ListItemAvatar>
                    <Avatar alt="Cindy Baker" src={avatarUrl} />
                    </ListItemAvatar>
                    <ListItemText
                    primary={name}
                    secondary={
                        <React.Fragment>
                        <Typography
                            sx={{ display: 'inline' }}
                            component="span"
                            variant="body2"
                            color="text.primary"
                        >
                            Sandra Adams
                        </Typography>
                        {oneLineIntroduction}
                        </React.Fragment>
                    }
                    />
                </ListItem>
            </List>
    )
}