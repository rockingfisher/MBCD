<template>
  <div>
    <div
      class="row"
      v-if="comment.review_id == review_id"
      v-show="!IsUpdateCommentBar"
    >
      <th class="col-6">
        {{ comment.content }}
      </th>
      <th class="col-3"></th>
      <button class="col-1" @click.prevent="deleteComment">삭제</button>
      <button class="col-1" @click.prevent="toggle_bar">수정</button>
      <hr />
    </div>
    <div class="row" v-show="IsUpdateCommentBar">
      <input class="col-6" type="text" v-model="content_input" />
      <th class="col-3"></th>
      <button class="col-1" @click.prevent="deleteComment">삭제</button>
      <button class="col-1" @click.prevent="updateComment">수정</button>
      <hr />
    </div>
  </div>
</template>

<script>
import axios from "axios";
export default {
  name: "CommentItem",
  data() {
    return {
      content_input: null,
      IsUpdateCommentBar: false,
    };
  },
  props: {
    comment: Object,
    review_id: Number,
  },
  methods: {
    deleteComment() {
      axios({
        method: "delete",
        url: `http://127.0.0.1:8000/community/comments/${this.comment.id}/`,
      })
        .then((res) => {
          console.log(res.data);
          this.$router.go();
          // this.$router.push({ name: "CommunityView" });
          // this.comments = res.data;
        })
        .catch((err) => {
          console.log(err);
          // console.log(review_id);
        });
    },
    toggle_bar() {
      this.IsUpdateCommentBar = !this.IsUpdateCommentBar;
      this.content_input = this.comment.content;
    },
    updateComment() {
      const content = this.content_input;
      const review_id = this.comment.review_id;

      if (!content) {
        alert("댓글을 입력해주세요");
        return;
      }

      axios({
        method: "put",
        url: `http://127.0.0.1:8000/community/comments/${this.comment.id}/`,
        data: {
          content,
          review_id,
        },
      })
        .then((res) => {
          console.log(res);
          this.toggle_bar();
          this.$router.go();
        })
        // this.comment_input = "";
        // this.getcomments();
        .catch((err) => console.log(err));
    },
  },
};
</script>

<style></style>
