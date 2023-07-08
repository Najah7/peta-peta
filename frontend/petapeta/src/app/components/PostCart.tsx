import PostIt from "./PostIt";

function PostCard() {
  return (
    <div className="post-card">
      <div className="post-card-username">username</div>
      <img width="100%" src="/chise.jpg"></img>
      <div style={{ display: "flex", justifyContent: "center" }}>
        <PostIt comment="美味しそう" />
        <PostIt comment="くさそう" />
        <PostIt comment="これはいいチーズ" />
      </div>
      <div className="post-card-comment">
        commentcommentcommentcommentcommentcommentcommentcommentcomment
      </div>
    </div>
  );
}

export default PostCard;
