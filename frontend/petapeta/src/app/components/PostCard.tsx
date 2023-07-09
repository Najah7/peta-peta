"use client";
import { Box, Center, Flex, Spacer } from "@chakra-ui/react";
import Stickeys from "./Stickeys";

type StickeysProps = {
  top: number;
  left: number;
  comment: string;
};

type PostCardProps = {
  username: string;
  comment: string;
  imgPath: string;
  note: number;
  post: StickeysProps[];
};
function PostCard(props: PostCardProps) {
  return (
    <>
      <Box m="30px">stickey notes:{props.note}</Box>
      <Center>
        <Box w="50vw">
          <Flex alignItems="center">
            <img
              style={{ width: "60px", height: "60px", borderRadius: "50%" }}
              src="/OIP.jpg"
            ></img>
            <div>{props.username}</div>
            <Spacer />
            <div>コメント:{props.comment}</div>
            <></>
          </Flex>
          <Center>
            <img width="100%" src={props.imgPath}></img>
          </Center>
        </Box>
      </Center>
      {props.post.map((post) => {
        return (
          <Stickeys top={post.top} left={post.left} comment={post.comment} />
        );
      })}
    </>
  );
}

export default PostCard;
