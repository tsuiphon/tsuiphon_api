window.onload = function() {
  // ボタンとモーダルを関連付ける
  $('.modal-trigger').leanModal({
    dismissible: true,  // 画面外のタッチによってモーダルを閉じるかどうか
    opacity: 0.1,       // 背景の透明度
    in_duration: 300,   // インアニメーションの時間
    out_duration: 200,  // アウトアニメーションの時間
    // 開くときのコールバック
    ready: function() {
      console.log('ready');
    },
    // 閉じる時のコールバック
    complete: function() {
      console.log('closed');
    }
  });
};
