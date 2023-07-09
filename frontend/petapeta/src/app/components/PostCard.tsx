"use client";
import { Box, Center, Flex, Spacer } from "@chakra-ui/react";
function PostCard() {
  return (
    <>
      <Box m="30px">stickey notes:15</Box>
      <Center>
        <Box w="50vw">
          <Flex alignItems="center">
            <img
              style={{ width: "60px", height: "60px", borderRadius: "50%" }}
              src="/OIP.jpg"
            ></img>
            <div>ユーザ名</div>
            <Spacer />
            <div>コメント:テスト用の画像です</div>
            <></>
          </Flex>
          <Center>
            <img width="100%" src="/tmp.jpg"></img>
          </Center>
        </Box>
      </Center>
      <Box
        w="100px"
        h="100px"
        bg="#ec7b26"
        position="relative"
        top="-400"
        left="500"
        p="10px"
        borderRadius="20px"
        opacity="0.8"
      >
        dsafafsafa
      </Box>
    </>
  );
}

export default PostCard;
