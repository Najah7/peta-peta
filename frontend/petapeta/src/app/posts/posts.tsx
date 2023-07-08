import PostCard from "../components/postCard/postCard";
import userForCard from "../data/user";
import postForCard from "../data/post";


const Posts: React.FC = (): JSX.Element => {
    return (
        <PostCard post={postForCard} user={userForCard}/>
    );
}

export default Posts;