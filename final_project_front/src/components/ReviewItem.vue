<template>
  <div>
    <router-link
      :to="{ name: 'ReviewDetailView', params: { review_id: review.id } }"
    >
      <th>게시글 번호: {{ review.id }}</th>
      <th>게시글 제목: {{ review.title }}</th>
      <th>작성자: {{ review.username }}</th>
    </router-link>
  </div>
</template>

<script>
export default {
  name: "ReviewItem",
  props: {
    review: Object,
  },
};
</script>

<style></style>
